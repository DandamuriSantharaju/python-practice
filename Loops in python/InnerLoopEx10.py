
#InnerLoopEx10.py
n=int(input("Enter how many values u have printed:"))
if n<=0:
    print("Invalid input")
else:
    lst=[]
    for i in range(0,n):
        lst.append(input("Enter {} value:".format(i)))
    else:
        print("List of values")
        print(lst)
        novovel = []
        for word in lst:
            res=True
            for ch in word:
                if ch.lower() in list("aeiou"):
                    res=False
                    break
            if res:
               novovel.append(word)
        print(novovel)