# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# https://www.geeksforgeeks.org/degrees-and-radians-in-python/

# Python code to demonstrate
# working of radians()
# Code #1 : Demonstrating radians() 
 
# for radians
import math
 
# Printing radians equivalents.
print("180 / pi Degrees is equal to Radians : ", end ="")
print (math.radians(180 / math.pi))
 
print("180 Degrees is equal to Radians : ", end ="")
print (math.radians(180))
 
print("1 Degrees is equal to Radians : ", end ="")
print (math.radians(1))

"""
Output:

180/pi Degrees is equal to Radians : 1.0
180 Degrees is equal to Radians : 3.141592653589793
1 Degrees is equal to Radians : 0.017453292519943295


Code #2 : Demonstrating degrees() 
"""

# Python code to demonstrate
# working of degrees()
 
# for degrees()
import math
 
# Printing degrees equivalents.
print("pi / 180 Radians is equal to Degrees : ", end ="")
print (math.degrees(math.pi / 180))
 
print("180 Radians is equal to Degrees : ", end ="")
print (math.degrees(180))
 
print("1 Radians is equal to Degrees : ", end ="")
print (math.degrees(1))

"""
Output:

pi/180 Radians is equal to Degrees : 1.0
180 Radians is equal to Degrees : 10313.240312354817
1 Radians is equal to Degrees : 57.29577951308232
Application : There are many possible applications of these functions in mathematical computations related to geometry and has a certain applications in astronomical computations as well.
"""

# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
# https://www.codespeedy.com/how-to-convert-radian-to-degree-in-python/
"""
Using formula(The obvious method)
We all know the formula for converting radian into degree,
degree=(radian*180)/pi
"""
import math
def degree(x):
    pi=math.pi
    degree=(x*180)/pi
    return degree

def radian(x):
    return (x * math.pi)/180

import math
def degree(x):
    x=math.degrees(x)
    return x

print(radian(1))

# https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/




