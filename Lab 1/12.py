#Check a given no is divisible by both 3 and 6.

Num=int(input("Enter a number:"))

if(Num%3 and Num%6 == 0):
    print("Number is divisible by 3 and 6 both.")
elif(Num % 3==0 and Num % 6 !=0):
    print ("Number is divisible by only 3.")

else:
    print("Number is not divisible by 3 or 6.")