import arcpy
from arcpy import env

try:
	arcpy.env.workspace = r"C:\EsriPress\Exercise8\Newark.gdb"
	arcpy.Buffer_analysis("NewarkCityLimit","CityLimitsBuffer","1000 feet")

except:
	print "The script has failed, which is surprising considering how little there is to screw up."
