from robodk import *
from robolink import *
from Init import init
import time


#    X, Y, Z, RX, RY, RZ
pickPosTable = (
    []
)

#    X, Y, Z, RX, RY, RZ
placePosTable = (
    []
)

def Calc_PickPos (nBlock):
    pickPos = ([0,0,0,0,0,0])
    for i in range(0,6):
        pickPos[i] = pickPosTable[nBlock][i]
    return pickPos

def Calc_PlacePos ():
    placePos = ([0,0,0,0,0,0])
    for i in range(0,6):
        placePos[i] = placePosTable[nBlock][i]
    return placePos