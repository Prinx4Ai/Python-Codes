#Pyramid Number Pattern.

n=int(input("Enter the number of Line in the Pattern:"))
for i in range(0,n+1):
     print(" " * (n - i), end="")  # Spaces for centering
     print((str(i) + " ") * i)