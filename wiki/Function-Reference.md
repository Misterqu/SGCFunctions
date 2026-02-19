# Function Reference

This page documents every public function exported by this mod under the `sgc_utils_fnc_` namespace.

## `sgc_utils_fnc_teleportPlayersInList`

**Purpose:** Teleport player units from a provided array to a destination and optionally set facing direction.

**Execution:** Can be called anywhere. It only teleports entries that are actual players.

### Parameters

1. `ARRAY` **_units**
2. `ARRAY` **_destination**
3. `NUMBER` **_direction** *(optional, default: `-1`)*

### Returns

- `NUMBER` — Count of players teleported.

### Example

```sqf
private _count = [thisList, [5000, 5000, 0], 180] call sgc_utils_fnc_teleportPlayersInList;
hint format ["Teleported %1 players", _count];
```

---

## `sgc_utils_fnc_createGlobalMarker`

**Purpose:** Create or update a global marker for all machines.

**Execution:** **Server-only behavior.** If called on a non-server machine, it exits early and returns the marker name without creating/updating it.

### Parameters

1. `STRING` **_name**
2. `ARRAY` **_position**
3. `STRING` **_text** *(optional, default: `""`)*
4. `STRING` **_color** *(optional, default: `"ColorRed"`)*
5. `STRING` **_type** *(optional, default: `"mil_dot"`)*

### Returns

- `STRING` — Marker name. Returns `""` when `_name` is empty.

### Example

```sqf
if (isServer) then {
    [
        "mission_marker_1",
        [5000, 5000, 0],
        "Primary Objective",
        "ColorRed",
        "mil_objective"
    ] call sgc_utils_fnc_createGlobalMarker;
};
```

---

## `sgc_utils_fnc_spawnGroup`

**Purpose:** Spawn an AI group with configurable side, size, class, and spread.

**Execution:** **Server-only.** Non-server calls return `grpNull`.

### Parameters

1. `ARRAY` **_spawnPos**
2. `SIDE` **_side** *(optional, default: `east`)*
3. `NUMBER` **_groupSize** *(optional, default: `6`)*
4. `STRING` **_unitClass** *(optional, default: `"O_Soldier_F"`)*
5. `NUMBER` **_radius** *(optional, default: `5`)*

### Returns

- `GROUP` — Created group object.

### Example

```sqf
if (isServer) then {
    private _grp = [[5000, 5000, 0], east, 6, "O_Soldier_F", 5] call sgc_utils_fnc_spawnGroup;
};
```

---

## `sgc_utils_fnc_addMoveWaypoint`

**Purpose:** Add a MOVE waypoint to an existing group.

### Parameters

1. `GROUP` **_group**
2. `ARRAY` **_position**
3. `NUMBER` **_radius** *(optional, default: `0`)*

### Returns

- `ARRAY` — Waypoint handle as returned by `addWaypoint`.
- Returns `[]` if `_group` is null.

### Example

```sqf
if (isServer) then {
    private _grp = [[5000, 5000, 0], east, 6, "O_Soldier_F", 5] call sgc_utils_fnc_spawnGroup;
    private _wp = [_grp, [5100, 5100, 0], 0] call sgc_utils_fnc_addMoveWaypoint;
};
```

---

## `sgc_utils_fnc_sendIntelToSide`

**Purpose:** Send intel to all alive players on a specific side, with optional marker update, diary entry, and timed hint text.

**Execution:** **Server-only.** Non-server calls return `0`.

### Parameters

1. `SIDE` **_targetSide** *(optional, default: `west`)*
2. `STRING` **_hintText**
3. `NUMBER` **_hintDuration** *(optional, default: `5`)*
4. `STRING` **_diaryTitle** *(optional, default: `"Intel"`)*
5. `STRING` **_diaryText**
6. `STRING` **_markerName**
7. `STRING` **_markerText**
8. `ARRAY` **_markerPos**
9. `STRING` **_markerColor** *(optional, default: `"ColorRed"`)*
10. `STRING` **_markerType** *(optional, default: `"mil_warning"`)*

### Returns

- `NUMBER` — Count of players notified.

### Example

```sqf
if (isServer) then {
    private _notified = [
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

    diag_log format ["Intel sent to %1 players", _notified];
};
```
