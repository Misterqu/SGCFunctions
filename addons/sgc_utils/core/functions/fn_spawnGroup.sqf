/*
    Author: SGC

    Description:
    Spawns an AI group with a configurable unit type and count.
    Should be called on server.

    Parameters:
    0: Spawn position [x,y,z] <ARRAY>
    1: Side <SIDE> (default: east)
    2: Group size <NUMBER> (default: 6)
    3: Unit classname <STRING> (default: O_Soldier_F)
    4: Radius/spread <NUMBER> (default: 5)

    Returns:
    Created group <GROUP>

    Example:
    private _grp = [[5000,5000,0], east, 6, "O_Soldier_F", 5] call sgc_utils_fnc_spawnGroup;
*/
params [
    ["_spawnPos", [0, 0, 0], [[]], 3],
    ["_side", east, [sideUnknown]],
    ["_groupSize", 6, [0]],
    ["_unitClass", "O_Soldier_F", [""]],
    ["_radius", 5, [0]]
];

if (!isServer) exitWith {grpNull};

private _group = createGroup _side;
private _count = _groupSize max 1;

for "_i" from 1 to _count do {
    _group createUnit [_unitClass, _spawnPos, [], _radius, "FORM"];
};

_group
