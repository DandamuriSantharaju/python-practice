
#negative numbers in a list.py
while(True):
    n = int(input("Enter how many values u have:"))
    if(n<=0):
        print("\t{} is invalid Number--try again".format(n))
        break
    else:
        lst=[]
        for i in range(0,n):
            val=(float(input("Enter {} value:".format(i))))
            lst.append(val)
        else:
            lst1 = []
            print("Given list of value={}".format(lst))
            for i in lst:
                if (i<0):
                    lst1.append(i)
            else:
                print("Negative numbers in a list={}".format(lst1))
                break
print("----------------------------------------------------------------")