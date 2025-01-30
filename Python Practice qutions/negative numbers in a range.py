
#negative numbers in a range.py
while(True):
    n=int(input("Enter how many values u have:"))
    if(n<=0):
        print("\t{} is invalid Number--try again".format(n))
    else:
        lst=[]
        for i in range(0,n):
            val=(float(input("Enter {} value:".format(i))))
            lst.append(val)
            print(i,end="")
        else:
            lst1=[]
            print("Given list of values={}".format(lst))
            for i in lst:
                if(i<0):
                    lst1.append(i)
            else:
                print("odd numbers in a List=".format(lst1))
                break
print("--------------------------------------------------------------")