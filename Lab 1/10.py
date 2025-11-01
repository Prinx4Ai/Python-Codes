#Program to calculate simple interest.

principleAmount=float(input("Enter the Principle Amount:"))

rate = float (input("Enter the rate of interst:"))

time = int (input("Enter time in years:"))

simpleInterest=(principleAmount * rate*time)/100

print("The simple interst will be:",simpleInterest)