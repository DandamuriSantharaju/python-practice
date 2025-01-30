n=int(input("Enter Howmany Values Used in List:"))
if(n<=0):
    print("{} is Invalid Input.".format(n))
else:
    lst=[]
    for val in range(1,n+1):
        lst.append(input("Enter {} Value:".format(val)))
    else:
        print("Given Elements of List")
        print(lst)
        pval=[]
        for word in lst:
            if not any(ch in list("aeiouAEIOU") for ch in word):
                    pval.append(word)
        else:
            print("Not Vowel Elements of List")
            print(pval)