#String manipulation

c="hello world"

#I.Convert into upper case
print("Upper Case:")
print(c.upper())

#II.Convert into lower case
print("Lower Case:")
print(c.lower)

#III.Convert into reverse string
print("reverse of the String is:")
print(c[::-1])

#IV.Count no. of vowels
vowels="aeiouAEIOU"
count=0
for char in c:
    if char in vowels:
        count += 1
print("No of Vowels:",count)