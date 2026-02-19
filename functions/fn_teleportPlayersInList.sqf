/*
    Author: SGC

    Description:
    Teleports player units from a supplied list to a destination and direction.

    Parameters:
    0: Units list <ARRAY>
    1: Destination ATL position <ARRAY>
    2: Direction in degrees <NUMBER> (default: current direction)

    Returns:
    Number of players teleported <NUMBER>

    Example:
    [thisList, [5000, 5000, 0], 180] call sgc_utils_fnc_teleportPlayersInList;
*/
params [
    ["_units", [], [[]]],
    ["_destination", [0, 0, 0], [[]], 3],
    ["_direction", -1, [0]]
];

private _teleported = 0;

{
    if (isPlayer _x) then {
        _x setPosATL _destination;

        if (_direction >= 0) then {
            _x setDir _direction;
        };

        _teleported = _teleported + 1;
    };
} forEach _units;

_teleported
