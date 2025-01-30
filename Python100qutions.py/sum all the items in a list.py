#1. Write a Python program to sum all the items in a list.
#sum all the items in a list.
lst=[10,20,30,50,-98]
s=0
r=[]
for i in lst:
    r.append(i)
    s = s + i
else:
    print(r)
    print("Sum of List=",s)
print("============================================================")
n=int(input("Enter How many values u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    s=0
    for i in range(0,n):
        val=float(input("Enter {} value:".format(i)))
        lst.append(val)
        s = s + val
    else:
        print("Given List")
        print(lst)
        print("Sum of List=",s)
print("===============================================================")
n=int(input("Enter How many values u have:"))
if(n<=0):
    print("{} is Invalid input--try again".format(n))
else:
    lst=[]
    s=0
    i=0
    while(n>i):
        val=float(input("Enter {} value:".format(i)))
        lst.append(val)
        s=s+val
        i=i+1
    else:
        print("Given List")
        print(lst)
        print("Sum of List=",s)
