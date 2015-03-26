f = open('c:/EsriPress/ArcpyBook/data/N_America.A2007275.txt','r')
lstFires = f.readlines()
for fire in lstFires:
	lstValues = fire.split(",")
	latitude = float(lstValues[0])
	longitude = float(lstValues[1])
	confid = int(lstValues[8])
	print "The latitude is: " + str(latitude) + " The longitude is: " + str(longitude) + " The confidence values is: " + str(confid)

f.close()
