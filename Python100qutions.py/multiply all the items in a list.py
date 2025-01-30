# Write a Python program to multiply all the items in a list.
#multiply all the items in a list.py
n=int(input("Enter How Many Numbers u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    s=1
    for i in range(1,n+1):
        val=float(input("Enter {} value:".format(i)))
        lst.append(val)
        s=s*val
    else:
        print("Given List")
        print(lst)
        print("Mul of=",s)
print("=========================================================")
n=int(input("Enetr How Many Values u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    s=1
    i=0
    while(n>i):
        val=float(input("Enter {} value:".format(i)))
        lst.append(val)
        s=s*val
        i = i + 1
    else:

        print("Given list")
        print(lst)
        print("MUL is =",s)
print("=======================================================")