# 3. Coordinate Geometry: Write a program that prompts the user to enter the (x, y)
# coordinates of a point. Determine and display which quadrant the point lies in (1st,
# 2nd, 3rd, or 4th), or if it lies on an axis or the origin.

x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0 and y > 0:
    print("Point lies in 1st Quadrant")
elif x < 0 and y > 0:
    print("Point lies in 2nd Quadrant")
elif x < 0 and y < 0:
    print("Point lies in 3rd Quadrant")
elif x > 0 and y < 0:
    print("Point lies in 4th Quadrant")
elif x == 0 and y == 0:
    print("Point lies at Origin")
elif x == 0:
    print("Point lies on Y-axis")
else:
    print("Point lies on X-axis")

