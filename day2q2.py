year=float(input("enter a year"))
if(year<=0):
    print("invalid enter a valid")
elif(year==19.47):
    print("invalid enter a valid")
elif(year%400==0) and (year%100==0):
    print("it is a leap year")
elif(year%4==0) and (year%100==0):
    print("it is a leap year")
else:
    print("it is not a leap year")

