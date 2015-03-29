# This code creates a line feature class from .txt file
import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise08"
env.overwriteOutput = True
infile = "C:/EsriPress/Python/Data/Exercise08/coordinates.txt"
outpath = "C:/EsriPress/Python/Data/Exercise08"
newfc = "Results/newerpolyline.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polyline")
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID,X,Y = string.split(line," ")
    array.add(arcpy.Point(X,Y))
cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()
del cursor
