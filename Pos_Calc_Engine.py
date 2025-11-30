from robodk import *
from robolink import *
import time


#    X, Y, Z, RX, RY, RZ
pickPosTable = (
    [72.5, 97.5, 15.0, 0.0, 0.0, 90],
    [97.5, 97.5, 15.0, 0.0, 0.0, 90],
    [122.5, 97.5, 15.0, 0.0, 0.0, 90],
    [147.5, 97.5, 15.0, 0.0, 0.0, 90],
    [172.5, 97.5, 15.0, 0.0, 0.0, 90],
    [197.5, 97.5, 15.0, 0.0, 0.0, 90],
    [222.5, 97.5, 15.0, 0.0, 0.0, 90],
    [247.5, 97.5, 15.0, 0.0, 0.0, 90],
    [72.5, 172.5, 15.0, 0.0, 0.0, 90],
    [97.5, 172.5, 15.0, 0.0, 0.0, 90],
    [122.5, 172.5, 15.0, 0.0, 0.0, 90],
    [147.5, 172.5, 15.0, 0.0, 0.0, 90],
    [172.5, 172.5, 15.0, 0.0, 0.0, 90],
    [197.5, 172.5, 15.0, 0.0, 0.0, 90],
    [222.5, 172.5, 15.0, 0.0, 0.0, 90],
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