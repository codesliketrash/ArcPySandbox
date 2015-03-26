import os
import zipfile

zfile = zipfile.ZipFile("shapefiles2.zip", "w", zipfile.ZIP_DEFLATED)

files = os.listdir("c:/EsriPress/ArcpyBook/data")

for f in files:
	if f.endswith("shp") or f.endswith("dbf") or f.endswith("shx"):
		zfile.write("C:/EsriPress/ArcpyBook/data/" + f)

for f in zfile.namelist():
	print "Added %s" % f

zfile.close()
