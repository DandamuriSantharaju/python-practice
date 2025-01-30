
#ContinueEx7.py
n=int(input("Enter How many values u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(float(input("Enter {} value:".format(i))))
    else:
        print("------------------------------------------------")
        print("Given List of values")
        print(lst)
        plist=[]
        print("------------------------------------------------")
        ps=0
        for val in lst:
            if(val<=0):
                continue
            plist.append(val)
            ps = ps + val
        else:
            print("Positive elements={}".format(plist))
            print("Positive Elements Sum={}".format(ps))
            print("-----------------------------------")
            nlist=[]
            ns=0
            for val in lst:
                if(val>=0):
                    continue
                nlist.append(val)
                ns=ns+val
            else:
                print("Negative elements={}".format(nlist))
                print("Negative Elements Sum={}".format(ns))
                print("-----------------------------------")
