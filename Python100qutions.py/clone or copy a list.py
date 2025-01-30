#Write a Python program to clone or copy a list.
#clone or copy a list.py
n=int(input("Enter How Many Values u have:"))
if(n<=0):
    print(f"{n} is invalid input")
else:
    lst1=[]
    lst2=[]
    for i in range(1,n+1):
        val=input("Enter {} value:".format(i))
        lst1.append(val)
        lst2=lst1
    else:
        print("Given List Is {}".format(lst1,id(lst1)))
        print("The Copy List Is {}".format(lst2,id(lst2)))