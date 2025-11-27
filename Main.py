#Init
from robodk import *
from robolink import *
from Init import init
import time
from Workflow_Manager import WorkFlowManagaer

RDK = Robolink()
robot = RDK.Item('Staubli TX2-90L')
robot_frame = RDK.Item("Staubli TX2-90L Base")

def init():
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
    WorkFlowManagaer(robot)


if __name__ == "__main__":
    main()
    pass