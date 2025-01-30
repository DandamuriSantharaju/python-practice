#Write a Python program to remove duplicates from a list
#remove duplicates from a list.py
n=int(input("Enter How many values U have:"))
if(n<=0):
    print("{} is invaid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=input("Enter {} value:".format(i))
        lst.append(val)
    else:
        print("Given List=",lst)
        print("-------------------------------")
        print("Remove Duplicates From a List")
        print(list(set(lst)))
print("================================================")
n=int(input("Enter How many values U have:"))
if(n<=0):
    print("{} is invaid input".format(n))
else:
    lst=[]
    i=0
    while(n>i):
        val=input("Enter {} value".format(i))
        lst.append(val)
        i=i+1
    else:
        print("Given List=", lst)
        print("-------------------------------")
        print("Remove Duplicates From a List")
        print(list(set(lst)))
print("===============================================")