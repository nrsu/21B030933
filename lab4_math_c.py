import math
from math import pi
number=int(input())
length=int(input())
area=(length**2*number)/(4*math.tan(pi/number))
print(area)