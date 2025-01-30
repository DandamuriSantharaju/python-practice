#Write a Python program to check a list is empty or not
#check a list is empty or not.py
from itertools import count

n=int(input("Enter How many values U have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=input("Enter {} value:".format(i))
        lst.append(val)
    for val in lst:
        if len(val)==0:
            print("The List is empty")
            break
    else:
        print("The List is Not empty")
        print("Given List is ",lst)

























