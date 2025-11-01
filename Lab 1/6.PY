#given year is leap or not

year =int(input ("Enter any year to check:"))

if (year % 4==0 and year%100 !=0) or (year%400==0):

    print("Congratulation Enjoy an extra day in this year.")
else:
    print("Not a leap year.")



