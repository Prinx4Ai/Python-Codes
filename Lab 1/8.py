# Three angles can form a valid triangle or not.

num1 = float(input("Enter First Angle: "))
num2 = float(input("Enter Second Angle: "))
num3 = float(input("Enter Third Angle: "))

if num1 + num2 + num3:
    print("The Triangle is valid.")

else:
    print("The Triangle is Invalid.")