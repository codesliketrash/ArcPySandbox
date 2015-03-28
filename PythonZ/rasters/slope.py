import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "C:/EsriPress/Python/Data/Exercise09"
env.overwriteOutput = True
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    outraster = arcpy.sa.Slope("elevation", "PERCENT_RISE")
    outraster.save("slope_per")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst liscense is not available."
