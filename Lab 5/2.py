
"""String Slicing and Indexing
Write a python program that takes a string input and performs-:"""
str=input("Enter a string:")
#1.Prints the first 3 characters
print("First 3 characters are:",str[:3])

#2.Print the Last Two characters
print("Last 2 characters are:",str[-2::])

#3.Print the string with every second Character.
print("Every second Character string:",str[::2])
#4.Print the String in reverse using slicing.
print("Reversed String is:",str[::-1])