import arcpy.mapping as mapping

mxd = mapping.MapDocument(r"c:\EsriPress\ArcpyBook\Ch4\Crime_BrokenDataLinks.mxd")

BrokenDS = mapping.ListBrokenDataSources(mxd)
for layer in BrokenDS:
	print layer.name