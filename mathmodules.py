#pi
print("Area of circle")
import math
r = float(input("Enter the radius of the circle: "))
area = math.pi * r * r
print("Radius =", r)
print("Area of the circle =", area)
#sqrt
print("Finding distance using pythagoras theorem")
import math
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
distance = math.sqrt(a*a + b*b)
print("Distance =", distance)
#sin,cos
import math
angle = float(input("Enter angle in degrees: "))
rad = angle * math.pi / 180
sin_value = math.sin(rad)
cos_value = math.cos(rad)
print("Sine of", angle, "degrees =", sin_value)
print("Cosine of", angle, "degrees =", cos_value)


