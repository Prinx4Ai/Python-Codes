#Reverse the digit of a given number


num=int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit=num%10
    reversed_num=reversed_num * 10 + digit 
    num=num//10

print("Reversed number:", reversed_num)
