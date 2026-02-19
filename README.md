# SGCFunctions (Arma 3 utility-function mod)

![SGC Logo](.docs/SGC.svg)

This repo contains an Arma 3 mod that exposes reusable SQF helper functions under the `sgc_utils_` prefix via `CfgFunctions`.

## Repository layout

This repository is organized so addon source content is clearly separated from repo-only files:

- `addons/sgc_utils/config.cpp` - addon config that is packed into `sgc_utils.pbo`
- `addons/sgc_utils/functions/*.sqf` - exported SQF function implementations
- `addons/sgc_utils/$PBOPREFIX$` - PBO prefix definition
- `mod.cpp` - launcher metadata for the mod
- `docs/`, `pages/`, `.github/`, `tools/` - documentation and development tooling (not packed into the addon)

## What mission makers get

No mission-side `.sqf` files are required. If the mod is loaded, mission makers can call:

- `sgc_utils_fnc_teleportPlayersInList`
- `sgc_utils_fnc_createGlobalMarker`
- `sgc_utils_fnc_spawnGroup`
- `sgc_utils_fnc_addMoveWaypoint`
- `sgc_utils_fnc_sendIntelToSide`

## Full function reference

A GitHub Pages-friendly reference for all exported functions is available under `pages/` (start at `pages/index.html`).

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
