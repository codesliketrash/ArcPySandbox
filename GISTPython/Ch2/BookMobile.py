import arcpy
from arcpy import env
arcpy.env.workspace = r"C:\EsriPress\GISTPython\Data\City of Oleander.gdb\\"
env.overwriteOutput = True

# set up cursor for the target sites
arcpy.MakeFeatureLayer_management("Parcels","Parcels_lyr",'"DU"=1')
arcpy.MakeFeatureLayer_management("BookmobileLocations","Locations_lyr")

siteCursor = arcpy.da.SearchCursor("Locations_lyr","Marker")
for row in siteCursor:
	siteName =row[0]
	arcpy.Select_analysis("Locations_lyr",r"C:\EsriPress\GISTPython\MyExercises\Scratch\TempStorage.gdb\SiteTemp",'"Marker" = \'' + siteName + "\'")
	arcpy.SelectLayerByLocation_management("Parcels_lyr","WITHIN_A_DISTANCE",r"C:\EsriPress\GISTPython\MyExercises\Scratch\TempStorage.gdb\SiteTemp","150","NEW_SELECTION")
	arcpy.CopyFeatures_management("Parcels_lyr",r"C:\EsriPress\GISTPython\MyExercises\MyAnswers.gdb\\" + siteName.replace(" ","_"))
	print siteName + "Output OK!"

parcelCount = int(arcpy.GetCount_management("Parcels_lyr").getOutput(0))
print parcelCount
while parcelCount < 200:
	arcpy.SelectLayerByLocation_management("Parcels_lyr","WITHIN_A_DISTANCE","Parcels_lyr","150","ADD_TO_SELECTION")

	parcelCount = int(arcpy.GetCount_management("Parcels_lyr").getOutput(0))
	print parcelCount
	#exit while statement when count exceeds 200

myCount = 1
theCondition = True

while theCondition == True:
	if myCount == 8:
		theCondition = False
	else:
		print "The Current Count is " + str(myCount)
		myCount = myCount + 1

print "The processing is complete. The final count equals " + str(myCount) + "."