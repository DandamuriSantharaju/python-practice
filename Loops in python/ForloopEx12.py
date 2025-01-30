from selectors import SelectSelector

#ForloopEx12.py
n=int(input("Enter How many factorly natural Nums sum u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tNatural numbers with in {}".format(n))
    print("-"*50)
    f=1
    for i in range(1,n+1):
        f=i*f
    else:
        print("-"*50)
        print("factorial=({})={}".format(n,f))






