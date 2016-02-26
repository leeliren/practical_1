# q2_calc_cylinder_volume.py
# program to calculae cylinder volume

#import math
from math import * 


# input radius
radius = float (input("enter radius: "))

# input length
length = float (input("enter length: "))

# compute cylinder area
area = radius * radius * pi

# compute cylinder volume
volume = area * length

#output cylinder volume
print("cylinder volume =", volume)
