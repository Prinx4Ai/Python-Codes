#Euclidean distance between two points in 2d space

import math

print("Enter First Number Details: ")
x1 =int (input("x1:"))  
y1 =int (input("y1:"))

print("Enter Second Number Details: ")
x2 =int (input("x2:"))  
y2 =int (input("y2:"))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean Distance between the points is:",distance)
