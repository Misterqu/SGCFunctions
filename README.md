# SGCFunctions (Arma 3 utility-function mod)

This repo contains an Arma 3 mod that exposes reusable SQF helper functions under the `sgc_utils_` prefix via `CfgFunctions`.

## What mission makers get

No mission-side `.sqf` files are required. If the mod is loaded, mission makers can call:

- `sgc_utils_fnc_teleportPlayersInList`
- `sgc_utils_fnc_createGlobalMarker`
- `sgc_utils_fnc_spawnGroup`
- `sgc_utils_fnc_addMoveWaypoint`
- `sgc_utils_fnc_sendIntelToSide`

## Quick trigger examples

### Teleport players in trigger list
```sqf
[thisList, [5000, 5000, 0], 180] call sgc_utils_fnc_teleportPlayersInList;
```

### Create objective marker
```sqf
if (isServer) then {
    ["mission_marker_1", [5000, 5000, 0], "Primary Objective", "ColorRed", "mil_objective"] call sgc_utils_fnc_createGlobalMarker;
};
```

### Spawn AI and assign waypoint
```sqf
if (isServer) then {
    private _grp = [[5000, 5000, 0], east, 6, "O_Soldier_F", 5] call sgc_utils_fnc_spawnGroup;
    [_grp, [5100, 5100, 0], 0] call sgc_utils_fnc_addMoveWaypoint;
};
```

### Send intel to BLUFOR + diary + marker
```sqf
if (isServer) then {
    [
        west,
        "Enemy mechanized units detected near AO.",
        5,
        "Enemy Movement",
        "Enemy mechanized units observed near AO. Stay alert.",
        "diary_marker_001",
        "Enemy Sighted",
        [5000, 5000, 0],
        "ColorRed",
        "mil_warning"
    ] call sgc_utils_fnc_sendIntelToSide;
};
```
