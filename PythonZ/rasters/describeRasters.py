import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.meanCellHeight
y = desc.meanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print " the raster resolution of Band 1 is " + str(x) + " by " + str(y) + "" + units + "."
print "The raster resolution is " + str(x) + " by " + str(y) + " " + units + "."
print "Raster base name is: " + desc.basename
print "Raster data type is: " + desc.dataType
print "Raster file extension is: " + desc.extension
print "Raster spatial reference is: " + desc.spatialReference.name
print "Raster format is: " + desc.format
print "Raster compression type is: + desc.compressionType"
print "Raster number of bands is: " + str(desc.bandCount)
