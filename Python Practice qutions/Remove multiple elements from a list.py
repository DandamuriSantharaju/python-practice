#Remove multiple elements from a list in Python
#Remove multiple elements from a list.py
# lst1=[10,20,30,40,50,60,70]
# print("lst1--->",lst1)
# del lst1[0:2]
# print(lst1)
# lst2=[10,20,30,40,50,60,70]
# print("lst2--->",lst2)
print("------------------------------------------------------------")
n=int(input("Enter how many values u have in list:"))
if(n<=0):
    print("Invalid Input")
else:
    lst=[]
    for i in range(1,n+1):
        lst.append(input("Enter {} value:".format(i)))
    else:
        print("-"*50)
        print("Given List")
        print(lst)
        print("-"*50)

