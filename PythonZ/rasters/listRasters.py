import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise09"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster
