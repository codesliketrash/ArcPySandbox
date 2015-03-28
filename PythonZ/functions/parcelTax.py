import parcelClass
myparcel = parcelClass.Parcel("SFR", 125000)
print "Land use: ", myparcel.landuse
mytax = myparcel.assessment()
print "Tax assessment: ", mytax
