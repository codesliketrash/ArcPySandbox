import arcpy

def listfieldnames(table):
    fields = arcpy.ListFields(table)
    namelist = []
    for field in fields:
        namelist.append(field.name)
    return namelist

fieldnames = listfieldnames("C:/EsriPress/Python/Data/Exercise12/streets.shp")
print fieldnames
