
#InnerLoopEx8.py
n=int(input("Enter the Range in which primes will de displayed:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    nop=0
    for i in range(2,n+1):
        print("-"*50)
        print(i)
        print("-"*50)
        res=True
        for j in range(2,i):
            if(i%j==0):
                res=False
                break
        if(res):
            print("\t\t\t{}".format(i))
            nop=nop+1
    else:
        print("--------------------------------------------------")
        print("Number of Primes within {}={}".format(n, nop))
        print("--------------------------------------------------")