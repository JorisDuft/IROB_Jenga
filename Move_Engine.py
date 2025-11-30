from robodk import *
from robolink import *
import time

RDK = Robolink()
robot = RDK.Item('Staubli TX2-90L')
robot_frame = RDK.Item("Staubli TX2-90L Base")

f_mag = RDK.Item("F_Magazinplatte")
f_tower = RDK.Item("F_Trumplatte")

def Move_PickPos(pickPos):
    robot.setFrame(f_mag)
    #Move to Pickup Position with vertical offset
    pickUpPosition = xyzrpw_2_pose([pickPos[0], pickPos[1], (pickPos[2]+25.0),pickPos[3], pickPos[4], pickPos[5]])
    robot.setAcceleration(150)
    robot.setSpeedJoints(20)
    robot.setSpeed(40)
    robot.MoveL(pickUpPosition)

    #Move down to Pickup Postition
    pickUpPosition = xyzrpw_2_pose([pickPos[0], pickPos[1], (pickPos[2]),pickPos[3], pickPos[4], pickPos[5]])
    robot.setAcceleration(50)
    robot.setSpeedJoints(20)
    robot.setSpeed(40)
    robot.MoveL(pickUpPosition)

    #Activate Vacume --> Pick up Block
    
    #Move up to Pickup Postition Witch vertical offset
    pickUpPosition = xyzrpw_2_pose([pickPos[0], pickPos[1], (pickPos[2]+25.0),pickPos[3], pickPos[4], pickPos[5]])
    robot.setAcceleration(150)
    robot.setSpeedJoints(10)
    robot.setSpeed(15)
    robot.MoveL(pickUpPosition)


def Move_PlacePos(placePos):
    robot.setFrame(f_tower)
    #Move to Place Position with vertical offset
    PlaceDownPosition = xyzrpw_2_pose([placePos[0], placePos[1], (placePos[2]+25.0), placePos[3], placePos[4], placePos[5]])
    robot.setAcceleration(150)
    robot.setSpeedJoints(20)
    robot.setSpeed(40)
    robot.MoveL(PlaceDownPosition)

    #Move down to Place Postition
    PlaceDownPosition = xyzrpw_2_pose([placePos[0], placePos[1], placePos[2], placePos[3], placePos[4], placePos[5]])
    robot.setAcceleration(50)
    robot.setSpeedJoints(10)
    robot.setSpeed(15)
    robot.MoveL(PlaceDownPosition)

    #Deactivate Vacume --> place up Block
    
    #Move up to Place Postition Witch vertical offset
    PlaceDownPosition = xyzrpw_2_pose([placePos[0], placePos[1], (placePos[2]+25.0), placePos[3], placePos[4], placePos[5]])
    robot.setAcceleration(150)
    robot.setSpeedJoints(20)
    robot.setSpeed(40)
    robot.MoveL(PlaceDownPosition)