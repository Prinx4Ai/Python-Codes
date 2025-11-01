#All odd number between 1 and 20 using a while loop and continue to skip even number


i = 1
while i<= 20:
    if i% 2==0:
        i=i+1
        continue
    print(i)
    i=i+1
