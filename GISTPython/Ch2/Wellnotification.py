try:
	import arcpy
	from arcpy import env
	env.workspace = r"C:\EsriPress\GISTPython\Data\City of Oleander.gdb\Well_Data"
	env.overwriteOutput = True

	fcName = "BC_Assoc_2H_Path"

	wellCursor = arcpy.da.SearchCursor(fcName,["Shape_Length"])
	for row in wellCursor:
		drillLength = row[0]
	if drillLength < 3000:
		wellBuffDist = 75
	elif drillLength >= 3000 and drillLength < 4000:
		wellBuffDist = 175
	else: 
		wellBuffDist = 300


	arcpy.Buffer_analysis(fcName,r"C:\EsriPress\GISTPython\MyExercises\Scratch\Temporary Storage.gdb\SelectionBuffer", wellBuffDist)

	arcpy.MakeFeatureLayer_management(r"C:\EsriPress\GISTPython\Data\City of Oleander.gdb\Parcels","Parcels_Lyr")

	arcpy.CopyRows_management("Parcels_lyr",r"C:\EsriPress\GISTPython\Data\\" + fcName + "_MailList.dbf")
	arcpy.SelectLayerByLocation_management("Parcels_lyr", "INTERSECT",r"C:\EsriPress\GISTPython\MyExercises\Scratch\TemporaryStorage.gdb\LightsBuffered")
except:
	print "Your script has failed miserably"