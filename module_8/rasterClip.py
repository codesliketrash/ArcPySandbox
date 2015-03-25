import arcpy
from arcpy import env
arcpy.env.extent
arcpy.env.workspace = r"C:/EsriPress/Exercise8/Newark.gdb"
try:
	raster = "studyarea"
	desc = arcpy.Describe(raster)
	clipExtent = str(desc.extent)
	print clipExtent
	print desc.dataType
	#clipeExtentb = "169572.946589085 184035.740526094 171777.630494665 185564.402571122"
	#print desc.extent
#	print desc.dataType
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Newark", "studyarea"
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Newark", "studyarea"
	arcpy.Clip_management(in_raster="Newark",rectangle="169572.946589085 184035.740526094 171777.630494665 185564.402571122",out_raster="C:/EsriPress/Exercise8/Newark.gdb/MyArea",in_template_dataset="studyarea",nodata_value="256",clipping_geometry="NONE",maintain_clipping_extent="NO_MAINTAIN_EXTENT")	
except:
	print "check the parameters of the Clip_management()"