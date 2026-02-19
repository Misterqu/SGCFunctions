#!/usr/bin/env python3
"""Lightweight SQF lint checks for CI.

Checks:
- trailing whitespace
- tab indentation
- unmatched (), [], {}
- missing newline at EOF
- params[] declaration shape
- basic command argument arity checks for common SQF commands
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys


@dataclass
class LintIssue:
    path: Path
    line: int
    message: str


def split_top_level_csv(text: str) -> list[str]:
    """Split a CSV-like expression while respecting nesting and quotes."""
    items: list[str] = []
    current: list[str] = []
    depth_round = depth_square = depth_curly = 0
    in_string = False
    escape = False

    for ch in text:
        if ch == '"' and not escape:
            in_string = not in_string
            current.append(ch)
            continue

        if in_string:
            escape = (ch == "\\") and not escape
            current.append(ch)
            continue

        if ch == "(":
            depth_round += 1
        elif ch == ")":
            depth_round = max(0, depth_round - 1)
        elif ch == "[":
            depth_square += 1
        elif ch == "]":
            depth_square = max(0, depth_square - 1)
        elif ch == "{":
            depth_curly += 1
        elif ch == "}":
            depth_curly = max(0, depth_curly - 1)

        if ch == "," and depth_round == depth_square == depth_curly == 0:
            items.append("".join(current).strip())
            current = []
        else:
            current.append(ch)

    tail = "".join(current).strip()
    if tail:
        items.append(tail)
    return items


def find_array_args_for_command(line: str, command: str) -> list[str]:
    """Extract array-argument payload from patterns like `cmd [a,b,c]`."""
    payloads: list[str] = []
    pattern = re.compile(rf"\b{re.escape(command)}\s*\[")
    start = 0
    while True:
        match = pattern.search(line, start)
        if not match:
            break

        i = match.end() - 1
        depth = 0
        in_string = False
        escape = False
        for j in range(i, len(line)):
            ch = line[j]
            if ch == '"' and not escape:
                in_string = not in_string
            if in_string:
                escape = (ch == "\\") and not escape
                continue
            if ch == "[":
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0:
                    payloads.append(line[i + 1 : j])
                    start = j + 1
                    break
        else:
            break
    return payloads




def strip_line_comment(line: str) -> str:
    """Remove // comments while preserving quoted strings."""
    out = []
    in_string = False
    escape = False
    i = 0
    while i < len(line):
        ch = line[i]
        nxt = line[i + 1] if i + 1 < len(line) else ""

        if ch == '"' and not escape:
            in_string = not in_string

        if not in_string and ch == "/" and nxt == "/":
            break

        if in_string:
            escape = (ch == "\\") and not escape
        else:
            escape = False

        out.append(ch)
        i += 1

    return "".join(out)
def lint_params_declaration(path: Path, lines: list[str], issues: list[LintIssue]) -> None:
    """Validate basic `params [...]` shape in function files."""
    if path.parent.name != "functions":
        return

    text = "".join(lines)
    if "params [" not in text:
        issues.append(LintIssue(path, 1, "Missing params declaration"))
        return

    param_line = re.compile(r'^\s*\[\s*"_[A-Za-z0-9]+"\s*,')
    in_params = False
    for index, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if not in_params and re.search(r"\bparams\s*\[", line):
            in_params = True
            continue
        if in_params:
            if re.match(r"^\s*\];\s*$", line):
                return
            if line.strip().startswith("[") and not param_line.match(line):
                issues.append(LintIssue(path, index, "Invalid params entry; expected [\"_name\", default, [types], ...]"))

    issues.append(LintIssue(path, 1, "Unclosed params declaration"))


def lint_command_arity(path: Path, lines: list[str], issues: list[LintIssue]) -> None:
    """Check arity for common SQF commands used in this repository."""
    signature_map = {
        "createMarker": 2,
        "createUnit": 5,
        "addWaypoint": 2,
        "remoteExecCall": 2,
    }

    for index, raw in enumerate(lines, start=1):
        line = strip_line_comment(raw.rstrip("\n"))
        for command, expected in signature_map.items():
            for payload in find_array_args_for_command(line, command):
                count = len(split_top_level_csv(payload))
                if count != expected:
                    issues.append(
                        LintIssue(
                            path,
                            index,
                            f"{command} expects {expected} argument(s) in array form, found {count}",
                        )
                    )


def strip_strings_and_line_comment(line: str) -> str:
    """Remove quoted strings and // comments for bracket scanning."""
    out = []
    in_string = False
    escape = False
    i = 0

    while i < len(line):
        ch = line[i]
        nxt = line[i + 1] if i + 1 < len(line) else ""

        if not in_string and ch == "/" and nxt == "/":
            break

        if ch == '"' and not escape:
            in_string = not in_string
            out.append(" ")
            i += 1
            continue

        if in_string:
            escape = (ch == "\\") and not escape
            out.append(" ")
            i += 1
            continue

        escape = False
        out.append(ch)
        i += 1

    return "".join(out)


def lint_file(path: Path) -> list[LintIssue]:
    issues: list[LintIssue] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    if text and not text.endswith("\n"):
        issues.append(LintIssue(path, max(1, len(lines)), "Missing trailing newline at end of file"))

    opening = {"(": ")", "[": "]", "{": "}"}
    closing = {")": "(", "]": "[", "}": "{"
    }
    stack: list[tuple[str, int]] = []

    for index, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")

        if line.rstrip(" \t") != line:
            issues.append(LintIssue(path, index, "Trailing whitespace"))

        if "\t" in line:
            issues.append(LintIssue(path, index, "Tab character found; use spaces"))

        scan_line = strip_strings_and_line_comment(line)
        for ch in scan_line:
            if ch in opening:
                stack.append((ch, index))
            elif ch in closing:
                if not stack or stack[-1][0] != closing[ch]:
                    issues.append(LintIssue(path, index, f"Unmatched closing '{ch}'"))
                else:
                    stack.pop()

    lint_params_declaration(path, lines, issues)
    lint_command_arity(path, lines, issues)

    for ch, line in stack:
        issues.append(LintIssue(path, line, f"Unclosed '{ch}'"))

    return issues


def collect_sqf_files() -> list[Path]:
    return sorted(Path("addons").glob("*/**/functions/*.sqf"))


def main() -> int:
    files = collect_sqf_files()
    if not files:
        print("No SQF files found.")
        return 0

    all_issues: list[LintIssue] = []
    for file in files:
        all_issues.extend(lint_file(file))

    for issue in all_issues:
        print(f"::error file={issue.path},line={issue.line}::{issue.message}")

    if all_issues:
        print(f"Found {len(all_issues)} lint issue(s) across {len(files)} SQF file(s).")
        return 1

    print(f"Lint passed for {len(files)} SQF file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
