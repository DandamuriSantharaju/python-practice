
#InnerLoopEx11.py
n=int(input("Enter how many values u have printed:"))
if n<=0:
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
        for val in lst:
           if(val<=0):
               continue
           print("----------------------------------------")
           print("Mul Table for :{}".format(val))
           print("----------------------------------------")
           for i in range(1,11):
               print("\t\t{} x {} ={}".format(val,i,val*i))