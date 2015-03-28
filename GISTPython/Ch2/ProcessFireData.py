import arcpy
from arcpy import env

try:
	env.workspace = r"C:\EsriPress\GISTPython\MyExercises\\"
	env.overwriteOutput = True

	inTable = arcpy.GetParameterAsText(0)
	fields = arcpy.ListFields(inTable)
	fieldinfo = arcpy.FieldInfo()

	for field in fields:
		if field.name == "inci_no":
			fieldinfor.addField(field.name,field.name,"VISIBLE")
		elif field.name == "alm_date":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "alm_time":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "arv_time":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "inci_type":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "descript":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "station":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "shift":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "city":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "number":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "st_prefix":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "street":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "st_type":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "st_suffix":
			fieldinfo.addField(field.name,field.name,"VISIBLE","")
		elif field.name == "addr_2":
			fieldinfo.addField(field.name,"GeoAddress","VISIBLE","")
		else:
			fieldinfo.addField(field.name,field.name,"HIDDEN","")	

	arcpy.MakeTableView_management(inTable,"fire_view","","",fieldinfo)

	arcpy.CalculateField_management("fire_view","GeoAddress","str(!number!) + ' ' + \
		!st_prefix!.strip() + ' ' + !street!.strip() + ' ' + !st_type!.strip() + ' ' + \
		!st_suffix!.strip()", "PYTHON")
	gdbName = "Fire_Files_For" + inTable[-8:]
	arcpy.CreateFieldGDB_management("C:\\EsriPress\\GISTPython\\MyExercises", gdbName)

	cityList = []

	for row in fireCursor:
		cityName = row[23]
		if cityName not in cityList:
			cityList.append(cityName)
		del row
		arcpy.AddWarning("Made the list of city names.")

	for name in cityList:
		cityQuery = '"city" = \'' +name + '\''
		arcpy.SelectLayerByAttribute_management("fire_view","NEW_SELECTION",cityQuery)

		newTable = "C:\\EsriPress\\GISTPython\\MyExercises\\" + gdbName + ".gdb\\" + name.replace(" ","_")

		arcpy.CopyRows_management("fire_view",newTable)

		itemCount = int(arcpy.GetCount_management("fire_view").getOutput(0))

		arcpy.AddWarning("A table called" + newTable + " was created with" + str(itemCount) + "rows.")
except: 
	print "The script has failed"