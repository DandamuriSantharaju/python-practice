#Program for Finding Max and Min from List of Values
#MaxMinValuesEx.py
n=int(input("How many value u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {} value :".format(i)))
        lst.append(val)
    else:
        rajumax=lst[0]
        rajumin=lst[0]
        for val in lst:
            if(val>rajumax):
                rajumax=val
            if(val<rajumin):
                rajumin=val
        else:
            print("Given values={}".format(lst))
            print("Max value={}".format(rajumax))
            print("Min value={}".format(rajumin))