#Init
from robodk import *
from robolink import *
import time
import random
from Workflow_Manager import WorkFlowManagaer

sim = True

RDK = Robolink()
robot = RDK.Item('Staubli TX2-90L')
robot_frame = RDK.Item("Staubli TX2-90L Base")

JengaBlocks = [ "JengaBlock1", "JengaBlock2", "JengaBlock3", "JengaBlock4", "JengaBlock5",
                "JengaBlock6", "JengaBlock7", "JengaBlock8", "JengaBlock9", "JengaBlock10",
                "JengaBlock11", "JengaBlock12", "JengaBlock13", "JengaBlock14", "JengaBlock15", 
]

JengaBlockPos = (
    [72.5, 97.5, 0.0, 0.0, 0.0, 90],
    [97.5, 97.5, 0.0, 0.0, 0.0, 90],
    [122.5, 97.5, 0.0, 0.0, 0.0, 90],
    [147.5, 97.5, 0.0, 0.0, 0.0, 90],
    [172.5, 97.5, 0.0, 0.0, 0.0, 90],
    [197.5, 97.5, 0.0, 0.0, 0.0, 90],
    [222.5, 97.5, 0.0, 0.0, 0.0, 90],
    [247.5, 97.5, 0.0, 0.0, 0.0, 90],
    [72.5, 172.5, 0.0, 0.0, 0.0, 90],
    [97.5, 172.5, 0.0, 0.0, 0.0, 90],
    [122.5, 172.5, 0.0, 0.0, 0.0, 90],
    [147.5, 172.5, 0.0, 0.0, 0.0, 90],
    [172.5, 172.5, 0.0, 0.0, 0.0, 90],
    [197.5, 172.5, 0.0, 0.0, 0.0, 90],
    [222.5, 172.5, 0.0, 0.0, 0.0, 90],
)

def init_sim():
    f_mag = RDK.Item("F_Magazinplatte")
    f_tower = RDK.Item("F_Trumplatte")
    f_mag.setPose(xyzrpw_2_pose([150.0, 800.0, 0.0, 0.0, 0.0, 180.0]))
    f_tower.setPose(xyzrpw_2_pose([529.0, -70.711, 0.0, 0.0, 0.0, 0.0]))
    for i in range(0, 15):
        JengaBlock = RDK.Item(JengaBlocks[i], ITEM_TYPE_OBJECT)
        JengaBlock.setParent(f_mag)
        JengaBlock.setPose(xyzrpw_2_pose([JengaBlockPos[i][0], JengaBlockPos[i][1], JengaBlockPos[i][2], JengaBlockPos[i][3], JengaBlockPos[i][4], JengaBlockPos[i][5]]))
        JengaBlock.setColor([random.random(),random.random(),random.random(),1])


def init():
    if(sim):
        init_sim()
    #Go to Home
    robot.setframe(robot_frame)
    homePos = xyzrpw_2_pose([385.0, 0, 100, 0.0, 180.0, 0.0])
    robot.setAcceleration(150)
    robot.setSpeedJoints(20)
    robot.setSpeed(40)
    robot.MoveL(homePos)



def main():
    init()
    #Start WorkFlowManager
    #WorkFlowManagaer(robot)


if __name__ == "__main__":
    main()
    pass