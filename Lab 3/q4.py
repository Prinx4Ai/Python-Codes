#Accept a number from the user and reverse it using a while loop.

num = int (input("Enter a Number:"))

reverse=0
original=num

while num!=0:
    digit=num%10
    reverse= reverse*10+digit
    num=num //10

print("Reversed Number:", reverse)