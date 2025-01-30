
#ContinueEx6.py
n=int(input("Enetr How many values u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(float(input("Enter {} values:".format(i))))
    else:
        print("-------------------------------------------------")
        print("Given list of values")
        print(lst)
        print("------------------------------------------------")
        plist=[]
        for val in lst:
            if(val<=0):
                continue
            if(val%2!=0):
                continue
            plist.append(val)
        print("List of given +ve even values")
        print(plist)
