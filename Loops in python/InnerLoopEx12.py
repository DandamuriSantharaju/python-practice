
#InnerLoopEx12.py
n=int(input("Enter how many values u have printed:"))
if(n<=0):
    print("Invalid input")
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(int(input("Enter {} value:".format(i))))
    else:
        print("-"*50)
        print("Given List")
        print(lst)
        print("-"*50)
        s=[]
        for val in lst:
            if(val<=1):
                continue
            res=True
            for i in range(2,val):
                if(val%i==0):
                    res=False
                    break
            if(res):
                s.append(val)
        print("Given list of prime value = ",s)
