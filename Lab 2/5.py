#Hollow Square Printing.


n = int(input("Enter the size of the square: "))

for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n)
    else:
        print('*' + ' ' *(n - 2) + '*')
