/*
    Author: SGC

    Description:
    Creates (or updates) a global marker. Should be called on server.

    Parameters:
    0: Marker name <STRING>
    1: Marker position [x,y,z] <ARRAY>
    2: Marker text <STRING> (default: "")
    3: Marker color <STRING> (default: "ColorRed")
    4: Marker type <STRING> (default: "mil_dot")

    Returns:
    Marker name <STRING>

    Example:
    ["mission_marker_1", [5000,5000,0], "Primary Objective", "ColorRed", "mil_objective"] call sgc_utils_fnc_createGlobalMarker;
*/
params [
    ["_name", "", [""]],
    ["_position", [0, 0, 0], [[]], 3],
    ["_text", "", [""]],
    ["_color", "ColorRed", [""]],
    ["_type", "mil_dot", [""]]
];

if (_name isEqualTo "") exitWith {""};
if (!isServer) exitWith {_name};

private _marker = createMarker [_name, _position];
_marker setMarkerPos _position;
_marker setMarkerText _text;
_marker setMarkerColor _color;
_marker setMarkerType _type;

_name
