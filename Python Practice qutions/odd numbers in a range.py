
#odd numbers in a range.py
while(True):
    n = int(input("Enter how many values u have:"))
    if (n <= 0):
        print("\t{} is invalid Number--try again".format(n))
        break
    else:
        lst=[]
        for i in range(1,n+2,2):
            lst.append(i)
        else:
            print(lst)
            break
print("--------------------------------------------------------------")