#Python program to find sum of elements in list
#sum of elements in list.py
# while(True):
#     n=int(input("Enter how many values u have in list:"))
#     if(n<=0):
#         print("\t{} is Invalid  Number--try again".format(n))
#     else:
#         lst=[]
#         s=0
#         for i in range(0,n):
#             val=float(input("Enter {} value:".format(i)))
#             lst.append(val)
#             s=val+s
#         print(lst)
#         print(s)
#         break
print("---------------------------------------------------------")
while(True):
    n=int(input("Enter how many values u have in list:"))
    if(n<=0):
        print("\t{} is Invalid  Number--try again".format(n))
    else:
        lst=[]
        s=0
        i=0
        while (i<n):
            val=float(input("Enter {} value:".format(i)))
            lst.append(val)
            s=s+val
            i=i+1
        else:
            print("Given list values={}".format(lst))
            print("Sum of liSt value is {}".format(s))
            break
print("----------------------------------------------------------")
