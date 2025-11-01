#take a num and calculate its factorial using while loop

number =int(input("Enter a Number:"))


fact = 1

while number > 1:
        fact =fact* number
        number=number - 1
print("The factorial is:", fact)