import arcpy
arcpy.env.workspace = "C:\EsriPress/Python/Data/Exercise12"
fields = arcpy.ListFields("streets.shp")
namelist = []
for field in fields:
    namelist.append(field.name)
print namelist
