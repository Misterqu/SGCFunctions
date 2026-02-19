/*
    Author: SGC

    Description:
    Adds a move waypoint to a group.

    Parameters:
    0: Group <GROUP>
    1: Waypoint position [x,y,z] <ARRAY>
    2: Waypoint radius <NUMBER> (default: 0)

    Returns:
    Waypoint <ARRAY>

    Example:
    [_grp, [5100,5100,0], 0] call sgc_utils_fnc_addMoveWaypoint;
*/
params [
    ["_group", grpNull, [grpNull]],
    ["_position", [0, 0, 0], [[]], 3],
    ["_radius", 0, [0]]
];

if (isNull _group) exitWith {[]};

private _wp = _group addWaypoint [_position, _radius];
_wp setWaypointType "MOVE";

_wp
