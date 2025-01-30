#Write a Python program to get the largest number from a list.
#largest number from a list.py
n=int(input("Enter How many values u have:"))
if(n<=0):
    print("{} is invalid input--try again".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=float(input("Enter {} value".format(i)))
        lst.append(val)
        s=max(lst)
    else:
        print("Given List")
        print(lst)
        print("Largest Number is =",s)
print("========================================================")
n=int(input("Enter How many values u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    i=0
    while(n>i):
        val=float(input("Enter {} value".format(i)))
        lst.append(val)
        s=max(lst)
        i=i+1
    else:
        print("Given List")
        print(lst)
        print("Largest Number is=",s)
print("======================================================")