import arcpy.mapping as mapping

mxd = mapping.MapDocument(r"c:\EsriPress\ArcpyBook\Ch4\Crime_BrokenDataLinks.mxd")

mxd.findAndReplaceWorkspacePaths(r"c:\EsriPress\ArcpyBook\Ch4\Data\OldData\CityOfSanAntonio.gdb", r"c:\EsriPress\ArcpyBook\Data\CityOfSanAntonio.gdb")

mxd.saveACopy(r"c:\EsriPress\ArcpyBook\Ch4\Crime_DataLinksFixed.mxd")