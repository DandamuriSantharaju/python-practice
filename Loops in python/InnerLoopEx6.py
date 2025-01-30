
#InnerLoopEx6.py
n=int(input("Enter how many mal table u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1):
        print("*"*50)
        print("Mul table of i=",i)
        print("*"*50)
        for j in range(1,11):
            print("\t{} x {}={}".format(i,j,i*j))
        else:
            print("-"*50)