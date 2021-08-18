import rhinoscriptsyntax as rs
import math
import random

#author Mesut Sala
#date August 2021

objects = rs.GetObjects("Pick your objects")

def randomRotate():
    for object in objects:
        if rs.IsCurve(object):
        
            point = rs.CurveAreaCentroid(object)[0]
            rs.RotateObjects(object, point, random.random()*360)
        
        else:
        
            boundingBox = rs.BoundingBox(object)
            boundingBoxCenter = (boundingBox[0]+boundingBox[6])/2
        
            rs.RotateObjects(object, boundingBoxCenter, random.random()*360)
            

if __name__=="__main__":
    randomRotate()