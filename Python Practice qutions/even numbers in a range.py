#Python program to print all even numbers in a range
#even numbers in a range.py
while(True):
    n = int(input("Enter how many values u have:"))
    if (n <= 0):
        print("\t{} is invalid Number--try again".format(n))
        break
    else:
        lst=[]
        for i in range(2,n+2,2):
            lst.append(i)
        else:
            print(lst)
            break
print("--------------------------------------------------------------")