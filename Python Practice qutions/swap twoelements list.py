
#swap twoelements list.py
# lst=[10,20,30,40,50,60]
# # lst[0:2],lst[4:6]=lst[-1:-3:-1],lst[-5:-6:-1]
# lst[0:2], lst[4:6] = lst[-1:-3:-1], lst[-5:-7:-1]
# print(lst)
#print("-----------------------------------------------------------------------------")
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
        lst[0:2], lst[4:6] = lst[-1:-3:-1], lst[-5:-7:-1]
        print(lst)




