#Write a program that checks whether a given number is Armstrong or not.

num = int(input("Enter a number: "))

digits = str(num)
n = len(digits)

sum_of_powers = sum(int(digit) ** n for digit in digits)

if num == sum_of_powers:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
