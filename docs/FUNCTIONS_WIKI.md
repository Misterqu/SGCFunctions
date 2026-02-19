# SGCFunctions Wiki: Function Reference & Usage

This page documents every public function exported by this mod under the `sgc_utils_fnc_` namespace.

## Getting started

- Load the mod on the server (and clients where required by your mission setup).
- Call functions from scripts, triggers, or mission logic using `call`.
- Server-only functions are marked below. For best results, wrap them in `if (isServer) then { ... };`.

---

## `sgc_utils_fnc_teleportPlayersInList`

**Purpose:** Teleport player units from a provided array to a destination and optionally set facing direction.

**Execution:** Can be called anywhere. It only teleports entries that are actual players.

### Parameters

1. `ARRAY` **_units**
   - Units to evaluate/teleport (for example, `thisList` from a trigger).
2. `ARRAY` **_destination**
   - Destination ATL position in the format `[x, y, z]`.
3. `NUMBER` **_direction** *(optional, default: `-1`)*
   - Facing direction in degrees.
   - If `< 0`, keeps each player's current direction.

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
   - Marker name/ID. Must be non-empty.
2. `ARRAY` **_position**
   - Marker position as `[x, y, z]`.
3. `STRING` **_text** *(optional, default: `""`)*
   - Visible marker text.
4. `STRING` **_color** *(optional, default: `"ColorRed"`)*
   - Marker color class.
5. `STRING` **_type** *(optional, default: `"mil_dot"`)*
   - Marker icon/type.

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
   - Spawn position as `[x, y, z]`.
2. `SIDE` **_side** *(optional, default: `east`)*
   - Side for the group.
3. `NUMBER` **_groupSize** *(optional, default: `6`)*
   - Number of units to create.
   - Values less than `1` are clamped to `1`.
4. `STRING` **_unitClass** *(optional, default: `"O_Soldier_F"`)*
   - Unit classname to spawn.
5. `NUMBER` **_radius** *(optional, default: `5`)*
   - Spawn spread radius passed to `createUnit`.

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

**Execution:** Can be called where group ownership/AI control is valid.

### Parameters

1. `GROUP` **_group**
   - Target AI group.
2. `ARRAY` **_position**
   - Waypoint position as `[x, y, z]`.
3. `NUMBER` **_radius** *(optional, default: `0`)*
   - Waypoint completion radius.

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

**Purpose:** Send intel to all alive players on a specific side:

- optional marker create/update,
- diary entry,
- timed hint text.

**Execution:** **Server-only.** Non-server calls return `0`.

### Parameters

1. `SIDE` **_targetSide** *(optional, default: `west`)*
   - Side to notify.
2. `STRING` **_hintText**
   - Hint text shown via `titleText`.
3. `NUMBER` **_hintDuration** *(optional, default: `5`)*
   - Hint duration in seconds.
4. `STRING` **_diaryTitle** *(optional, default: `"Intel"`)*
   - Diary record title.
5. `STRING` **_diaryText**
   - Diary body text.
6. `STRING` **_markerName**
   - Marker name/ID. If empty, no marker operation is performed.
7. `STRING` **_markerText**
   - Marker label text.
8. `ARRAY` **_markerPos**
   - Marker position `[x, y, z]`.
9. `STRING` **_markerColor** *(optional, default: `"ColorRed"`)*
   - Marker color.
10. `STRING` **_markerType** *(optional, default: `"mil_warning"`)*
    - Marker icon/type.

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

---

## Recommended usage patterns

- **Trigger-based teleport:** Use `thisList` directly with `sgc_utils_fnc_teleportPlayersInList`.
- **Server authority:** Create markers/spawn groups/send intel from server-side scripts.
- **Composable AI flow:** Spawn with `sgc_utils_fnc_spawnGroup`, then assign objectives with `sgc_utils_fnc_addMoveWaypoint`.
- **Single intel broadcast helper:** Use `sgc_utils_fnc_sendIntelToSide` when you want marker + diary + hint in one call.
