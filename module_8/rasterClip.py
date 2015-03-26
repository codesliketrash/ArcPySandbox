import arcpy
from arcpy import env
env.overwriteOutput = True
arcpy.env.workspace = r"C:/EsriPress/Exercise8/Newark.gdb"
try:
	raster = "studyarea"
	desc = arcpy.Describe(raster)
	clipExtent = str(desc.extent)
	print "The extent of the study area is:  " + clipExtent
	print desc.dataType
	arcpy.Clip_management("Newark",clipExtent,"MyArea")	
except:
	print "check to see if the parameters of the Clip_management() tool are valid"