#Write a program that takes 4-digit number from the user and check whether it is a narcissist number or not.

num = int(input("Enter a 4-digit number: "))

if 1000 <= num <= 9999:
    digits = str(num)
    sum_of_powers = sum(int(d)**4 for d in digits)

    if num == sum_of_powers:
        print(num, "is a narcissist number.")
        #Example-:1634 is a narcissist number.

    else:
        print(num, "is not a narcissist number.")
else:
    print("Please enter a valid 4-digit number.")
