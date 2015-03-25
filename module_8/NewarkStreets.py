import arcpy
from arcpy import env
arcpy.env.workspace = r"C:\EsriPress\Exercise8\Newark.gdb"
try:
	descFC = arcpy.Describe("NewarkStreets")		
	ext = descFC.extent
	print "The shape type is: " + descFC.shapeType
	print "The feature type is: " + descFC.featureType
	print "Spatial Index:  " + str(descFC.hasSpatialIndex)
	print  "the extent of the feature class =  "  
	print "XMIN: %f" % (ext.XMin) 
	print "YMin: %f" % (ext.YMin)
	print "XMax: %f" % (ext.XMax)
	print "YMax: %f" % (ext.YMax)
	print "Processing Complete"
except:
	print "The script has failed check your syntax and try again"
