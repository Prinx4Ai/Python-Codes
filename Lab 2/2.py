#Symmetric asteric Pattern
n=int(input("Enter the number of Line in the Pattern:"))

for i in range(1, n + 1):
    stars = i if i <= n // 2 + 1 else n - i + 1
    print("* " * stars)
