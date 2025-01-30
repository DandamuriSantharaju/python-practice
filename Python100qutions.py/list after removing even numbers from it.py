#Write a Python program to print the numbers of a specified list after removing even numbers from it.
#list after removing even numbers from it.py
n=int(input("Enter How many Values u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    lst1=[]
    for i in range(1,n+1):
        val=float(input("Enter {} Value:".format(i)))
        lst.append(val)
        if val%2!=0:
           lst1.append(val)
    else:
        print("Given list")
        print(lst)
        print("Removing even numbers From List")
        print(lst1)
print("====================================================================")





