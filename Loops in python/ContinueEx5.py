#Program for accepting List of Numerical values and Find only +Ve Values
##ContinueEx5.py
n=int(input("Enter How many values u have:"))
if(n<=0):
    print(f"{n} is invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(float(input("Enter {} value:".format(i))))
    else:
        print("-----------------------------------")
        print("Given List of values")
        print(lst)
        nlist=[]
        for val in lst:
            if val>=0:
                continue
            nlist.append(val)
        print("-------------------------------------")
        print(val)