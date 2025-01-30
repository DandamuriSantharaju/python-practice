#Python program to interchange first and last elements in a list
#interchange first&last elementslist.py
lst=[10,50,70,90,60,35]
lst[0],lst[5]=lst[5],lst[0]
print(lst)
#print("---------------------------------------------------------------------)
n=int(input("Enter How many value u have in lsist:"))
if(n<=0):
    print("{} is inbalid input--try again".format(n))
else:
    lst=[]
    for i in range(0,n):
        lst.append(input("Enter {} value:".format(i)))
           # lst[0],lst[-1]=lst[-1],lst[0]
    else:
        print("interchange first and last elements in a list")
        lst[0], lst[-1] = lst[-1], lst[0]
        print(lst)