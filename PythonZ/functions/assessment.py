# This script is  to be run from the terminal and to be given at argument. For example run python assessment.py SFR 125000

import sys
landuse = sys.argv[1]
value = int(sys.argv[2])

if landuse == "SFR":
    rate = 0.05
elif landuse == "MFR":
    rate = 0.04
else:
    rate = 0.02
assessment = value * rate
print assessment
