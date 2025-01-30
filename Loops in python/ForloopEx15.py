
#ForloopEx15.py
n=int(input("Enter How Many Value Sum and Avg u want to Find:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    s=0
    for i in range(1,n+1):
        val=float(input("enter {} value".format(i)))
        s=s+val
    else:
        print("-"*40)
        print("Sum={}".format(s))
        print("Average=%0.2f" % (s / n))




