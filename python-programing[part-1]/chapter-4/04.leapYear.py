# python3 chapter-4/04.leapYear.py

year = int(input("Enter Year "))
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")

if year % 100 != 0 and year % 4 == 0:
    print("Yes")
elif year % 100 == 0 and year % 400 == 0:
    print("Yes")
else:
    print("No")