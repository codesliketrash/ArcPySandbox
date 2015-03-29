# This script demonstrates how to list data frames within a particular .mxd.

import arcpy
mxd = "C:/EsriPress/Python/Data/Exercise10/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
listdf = arcpy.mapping.ListDataFrames(mapdoc)
for df in listdf:
    print df.name
del mapdoc
del listdf
