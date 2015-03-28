import arcpy
from arcpy import env
env.workspace = "C:\EsriPress\GISTPython\Data\StormDrainUtility.gdb" 
env.overwriteOutput = True

try:
	fixCount = int(arcpy.GetCount_management("Fixtures").getOutput(0)) 
	arcpy.AddWarning("The number of features selected is " + str(fixCount) + ".")
	if fixCount <> 1:
		arcpy.AddError("The number of selected features MUST be only one." + \
			" Prepare a new selection and try again.")
		raise exception
	else:
		arcpy.AddWarning("Only one feature is selected and the script is continuing ...")

	fixCursor = arcpy.da.SearchCursor("Fixtures", "System")
	for row in fixCursor:
		systemName = row[0]
		arcpy.AddWarning("You are working on the " + systemName + " system.")