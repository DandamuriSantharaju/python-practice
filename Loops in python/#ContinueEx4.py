#Program for accepting List of Numerical values and Find only +Ve Values
##ContinueEx4.py
n=int(input("Enter How many values u have:"))
if(n<=0):
    print(f"{n} is invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(float(input("Enter {} value:".format(i))))
    else:
        print("-----------------------------------")
        print("Given List of Values")
        print(lst)  # [100.0, -200.0, 300.0, -150.0, 40.0]
        print("-----------------------------------")
        plist=[]
        for val in lst:
            if(val<=0):
                continue
            plist.append(val)
        print("List of +Ve Values")
        print(plist)
