
#Multiply all numbers in the list.py
# while(True):
#     n=int(input("Enter how many values u have in list:"))
#     if(n<=0):
#         print("\t{} is Invalid  Number--try again".format(n))
#     else:
#         lst=[]
#         s=1
#         for i in range(0,n):
#             val=float(input("Enetr {} Value:".format(i)))
#             lst.append(val)
#             s=s*val
#         else:
#             print("Given list={}".format(lst))
#             print("MUL of list is {}".format(s))
#             break
print("-----------------------------------------------------")
while(True):
    n=int(input("Enter how many values u have in list:"))
    if(n<=0):
        print("\t{} is invalid Number--try again".format(n))
    else:
        lst=[]
        i=0
        s=1
        while (i<n):
            val=float(input("Enetr {} value:".format(i)))
            lst.append(val)
            s=s*val
            i=i+1
        else:
            print("Given list={}".format(lst))
            print("MUL of list is {}".format(s))
            break
print("---------------------------------------------------------")