n=int(input("Enter Howmany Values Used in List:"))
if(n<=0):
    print("{} is Invalid Input.".format(n))
else:
    lst=[]
    for val in range(1,n+1):
        lst.append(float(input("Enter {} Value:".format(val))))
    else:
        print("Given List of Elements")
        print(lst)
        prdlst=[]
        for i in lst:
            prdlst.append(i*i)
        else:
            print("Product List of Elements")
            print(prdlst)