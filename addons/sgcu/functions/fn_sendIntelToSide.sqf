/*
    Author: SGC

    Description:
    Creates/updates an intel marker and sends a diary entry + timed hint
    to all alive players on the provided side. Should be called on server.

    Parameters:
    0: Target side <SIDE> (default: west)
    1: Hint text <STRING>
    2: Hint duration seconds <NUMBER> (default: 5)
    3: Diary title <STRING>
    4: Diary text <STRING>
    5: Marker name <STRING>
    6: Marker text <STRING>
    7: Marker position [x,y,z] <ARRAY>
    8: Marker color <STRING> (default: ColorRed)
    9: Marker type <STRING> (default: mil_warning)

    Returns:
    Number of players notified <NUMBER>

    Example:
    [
        west,
        "Enemy mechanized units detected near AO.",
        5,
        "Enemy Movement",
        "Enemy mechanized units observed near AO. Stay alert.",
        "diary_marker_001",
        "Enemy Sighted",
        [5000,5000,0],
        "ColorRed",
        "mil_warning"
    ] call sgc_utils_fnc_sendIntelToSide;
*/
params [
    ["_targetSide", west, [sideUnknown]],
    ["_hintText", "", [""]],
    ["_hintDuration", 5, [0]],
    ["_diaryTitle", "Intel", [""]],
    ["_diaryText", "", [""]],
    ["_markerName", "", [""]],
    ["_markerText", "", [""]],
    ["_markerPos", [0, 0, 0], [[]], 3],
    ["_markerColor", "ColorRed", [""]],
    ["_markerType", "mil_warning", [""]]
];

if (!isServer) exitWith {0};

if (_markerName isNotEqualTo "") then {
    [_markerName, _markerPos, _markerText, _markerColor, _markerType] call sgc_utils_fnc_createGlobalMarker;
};

private _notified = 0;

{
    if (!isNull _x && {alive _x} && {side _x == _targetSide}) then {
        [_x, ["Diary", [_diaryTitle, _diaryText]]] remoteExecCall ["createDiaryRecord", _x];
        [_hintText, "PLAIN", _hintDuration] remoteExecCall ["titleText", _x];
        [0, _hintDuration] remoteExecCall ["titleFadeOut", _x];
        _notified = _notified + 1;
    };
} forEach allPlayers;

_notified
