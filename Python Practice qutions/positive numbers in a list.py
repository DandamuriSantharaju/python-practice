
#positive numbers in a list.py
# while(True):
#     n = int(input("Enter how many values u have:"))
#     if(n<=0):
#         print("\t{} is invalid Number--try again".format(n))
#         break
#     else:
#         lst=[]
#         for i in range(0,n):
#             val=(float(input("Enter {} value:".format(i))))
#             lst.append(val)
#         else:
#             lst1 = []
#             print("Given list of value={}".format(lst))
#             for i in lst:
#                 if (i>0):
#                     lst1.append(i)
#             else:
#                 print("Positive numbers in a list={}".format(lst1))
#                 break
print("----------------------------------------------------------------")
while(True):
    n=int(input("Enter How many values u have:"))
    if(n<=0):
        print("{} is invalid input ---try again".format(n))
    else:
        lst=[]
        i=0
        while(i<n):
            lst.append(float(input("Enter {} value".format(i))))
            i = i + 1
        else:
            lst1=[]
            if lst>0:
                lst1.append(lst)
            else:
                print(lst1)
                break