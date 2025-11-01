#Input a number and calcualte sum of digits

num = input ("Enter a number:")
sum = 0

for digit in num:
    if digit.isdigit():
        sum = sum + int(digit)

print("Sum of digits:", sum)
