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
    class StargateCommandFunctions {
        tags="SGCF";

        class functions {
            file = "sgcu\functions";

            class teleportPlayersInList {
               
            };
            class createGlobalMarker {
                
            };
            class spawnGroup {
              
            };
            class addMoveWaypoint {
               
            };
            class sendIntelToSide {
               
            };
        };
    };
};
