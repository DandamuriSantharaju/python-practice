#Python | Ways to check if element exists in list
#element exists in list.py
lst=[10,20,30,40,50,60]
print(lst)
while(True):
    n=int(input("Enter how many values u have in list:"))
    if(n<=0):
        print("{} is Invalid Input".format(n))
    else:
        lst=[]
        for i in range(1,n+1):
            lst.append(float(input("Enter {} value:".format(i))))
        else:
            print("--------------------------------------")
            print("Given List")
            print(lst)
            print("--------------------------------------")
            val=float(input("Enter element exists in list:"))
            if val in lst:
                print("-----------------------------------------")
                print("\t The element in list {}".format(val))
                print("============================================")
                break
            else:
                print("---------------------------------------------")
                print("\tThe element Does not in list {}".format(val))
                print("=============================================")
                break
