#Python program to find the smallest number in a list
#smallest number in a list.py
lst=[10,20,30,65,89,-45,78]
print(lst)
lst1=min(lst)
print(lst1)
# print("------------------------------------------------------------")
# while(True):
#     n=int(input("Enter how many values u have in list:"))
#     if(n<=0):
#         print("\t{} is invalid Number--try again".format(n))
#     else:
#         lst=[]
#         lst1=[]
#         for i in range(0,n):
#             lst.append(float(input("Enter {} value:".format(i))))
#             lst1=min(lst)
#         else:
#             print("Given List ={}".format(lst))
#             print("smallest number in a list is {}".format(lst1))
#             break
print("--------------------------------------------------------------")
while(True):
    n=int(input("Enter how many values u have in list:"))
    if(n<=0):
        print("\t{} is invalid Number--try again".format(n))
    else:
        lst=[]
        lst1=[]
        i=0
        while(i<n):
            val=float(input("Enter {} value:".format(i)))
            lst.append(val)
            lst1=min(lst)
            i=i+1
        else:
            print("Given List ={}".format(lst))
            print("smallest number in a list is {}".format(lst1))
            break
print("--------------------------------------------------------------")