# SGCFunctions Wiki

![SGC Logo](../SGC.svg)

Welcome to the SGCFunctions GitHub Wiki.

## What this mod provides

SGCFunctions is an Arma 3 utility-function mod that exposes reusable SQF helpers under the `sgc_utils_fnc_` namespace via `CfgFunctions`.

### Exported functions

- `sgc_utils_fnc_teleportPlayersInList`
- `sgc_utils_fnc_createGlobalMarker`
- `sgc_utils_fnc_spawnGroup`
- `sgc_utils_fnc_addMoveWaypoint`
- `sgc_utils_fnc_sendIntelToSide`

## Function documentation

- [Function Reference](Function-Reference)

## Notes

- Functions marked server-only should be called inside `if (isServer) then { ... };`.
- Usage examples for all functions are in the Function Reference page.
