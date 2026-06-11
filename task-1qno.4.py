# 4. Advanced Math: Write a program that takes a radius as input and calculates the
# following for a sphere: Diameter, Circumference, Surface Area, and Volume.
# Additionally, calculate the natural log of the volume.

import math

radius = float(input("Enter radius of sphere: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius**2
volume = (4/3) * math.pi * radius**3
log_volume = math.log(volume)

print("\nSphere Calculations")
print("-----------------------")
print("Diameter =", diameter)
print("Circumference =", circumference)
print("Surface Area =", surface_area)
print("Volume =", volume)
print("Natural Log of Volume =", log_volume)
