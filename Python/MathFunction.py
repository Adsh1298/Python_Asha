from codecs import xmlcharrefreplace_errors
import math
x=math.pi
y=-4
z=5
result=round(x)
result=abs(y)
result=max(x,y,z)
result=min(x,y,z)

result=math.ceil(x)
result=math.floor(x)
result=math.sqrt(81)
result=math.pow(3,4)
result=math.perm(8,5)
print(result)
#Example 1:#Circumference of a circle
# radius=float(input("Enter the radius of the circle: "))
# circumference=2*math.pi*radius
# print(f"The circumference of the circle  with radius {radius} is {circumference}cm")
# #Area of a circle
# radius=float(input("Enter the radius of the circle: "))
# Area =math.pi*pow(radius,2)
# print(f"The area of the circle  with radius {radius} is {Area}cm²")

#Find the hypotenuse of a Triangle:
a=float(input("Enter the lenght of Sise A: "))
b=float(input("Enter the lenght of Sise B: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The lenght of side C is {c}")
