pointX1 = float(input("Enter X1: "))
pointY1 = float(input("Enter Y1: "))
pointX2 = float(input("Enter X2: "))
pointY2 = float(input("Enter Y2: "))

import math
distBetween = math.sqrt((pointX2 - pointX1)**2 + (pointY2 - pointY1)**2)

print("Distance between point one and two is " + str(distBetween))
