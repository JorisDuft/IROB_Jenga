from robodk import *
from robolink import *
import time
from Move_Engine import *
from Pos_Calc_Engine import *




def WorkFlowManagaer (robot):
    nBlocks = 15
    move_Pos = ([0,0,0,0,0,0])
    for nBlock in range(0,nBlocks+1):
        move_pos = Calc_PickPos(nBlock)
        Move_PickPos(robot, move_pos)
        move_pos = Calc_PlacePos(nBlock)
        Move_PlacePos(robot, move_pos)