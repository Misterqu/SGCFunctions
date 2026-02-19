class CfgPatches {
    class SGCFunctions {
        name = "SGC Reusable SQF Functions";
        author = "SGC";
        requiredVersion = 2.10;
        requiredAddons[] = {"A3_Functions_F"};
        units[] = {};
        weapons[] = {};
    };
};

class CfgFunctions {
    class sgcu {
        class functions {
            file = "addons/sgcu/functions";

            class teleportPlayersInList {
                file = "addons/sgcu/functions/fn_teleportPlayersInList.sqf"
            };
            class createGlobalMarker {
                file = "addons/sgcu/functions/fn_createGlobalMarker.sqf"
            };
            class spawnGroup {
                file = "addons/sgcu/functions/fn_spawnGroup.sqf"
            };
            class addMoveWaypoint {
                file = "addons/sgcu/functions/fn_addMoveWaypoint.sqf"
            };
            class sendIntelToSide {
                file = "addons/sgcu/functions/fn_sendIntelToSide.sqf"
            };
        };
    };
};
