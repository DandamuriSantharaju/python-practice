
#ForloopEx9.py
n=int(input("Enter How many natural Nums sum u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("Natural Numbers with in {}".format(n))
    print("-"*50)
    s=0
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i
    else:
        print("-"*50)
        print("\tsum={}".format(s))
        print("-"*50)