from xml.dom import minidom

xmldoc = minidom.parse("WitchFireResidenceDestroyed.xml")
childNodes = xmldoc.childNodes
eList = childNodes[0].getElementsByTagName("fire")

for e in eList:
	if e.hasAttribute("address"):
		print e.getAttribute("address")


