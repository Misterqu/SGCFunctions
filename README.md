# SGCFunctions (Arma 3 utility-function mod)

This repo contains an Arma 3 mod that exposes reusable SQF helper functions under the `sgc_utils_` prefix via `CfgFunctions`.

## What mission makers get

No mission-side `.sqf` files are required. If the mod is loaded, mission makers can call:

- `sgc_utils_fnc_teleportPlayersInList`
- `sgc_utils_fnc_createGlobalMarker`
- `sgc_utils_fnc_spawnGroup`
- `sgc_utils_fnc_addMoveWaypoint`
- `sgc_utils_fnc_sendIntelToSide`

## Full function reference

A wiki-style reference for all exported functions is available at `docs/FUNCTIONS_WIKI.md`.

## CI linting for SQF

A GitHub Actions workflow is included at `.github/workflows/sqf-lint.yml`.
It runs `python3 tools/lint_sqf.py` on every pull request and on pushes to `main`/`master`.

Current lint checks:
- trailing whitespace
- tab characters
- unbalanced brackets `()[]{}`
- missing newline at end of file
- malformed `params [...]` entries in function files
- command arity checks for common array-style calls (`createMarker`, `createUnit`, `addWaypoint`, `remoteExecCall`)

The workflow emits GitHub annotation errors so issues are highlighted inline in PRs.
