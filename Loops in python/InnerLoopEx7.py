#InnerLoopEx7.py
import calendar
year=int(input("Enter the number which year u have printed:"))
if(year<=0):
    print("{} is invalid input".format(year))
else:
    print("-"*50)
    print("Year;{}".format(year))
    print("-"*50)
    for i in range(1,13):
        print(calendar.month(year,i))
    print("-"*50)