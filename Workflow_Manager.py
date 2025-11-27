from robodk import *
from robolink import *
from Init import init
import time
from Move_Engine import *
from Pos_Calc_Engine import *




def WorkFlowManagaer (robot):
    nBlock = 12
    move_Pos = ([0,0,0,0,0,0])
    for i in range(0,nBlock+1):
        move_pos = Calc_PickPos(nBlock)
        Move_PickPos(robot, move_pos)
        move_pos = Calc_PlacePos(nBlock)
        Move_PlacePos(robot, move_pos)