from selectors import SelectSelector

#ForloopEx11.py
n=int(input("Enter How many product natural Nums sum u want:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("\tNatural numbers with in {}".format(n))
    print("-"*50)
    p=1
    for i in range(1,n+1):
        print(i)
        p=p*i
    else:
        print("-"*50)
        print("Product={}".format(p))
        print("-"*50)







