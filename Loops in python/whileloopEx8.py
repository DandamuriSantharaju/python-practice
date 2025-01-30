
#whileloopEx8.py
n=int(input("Enter the natural number:"))
if(n==0):
    print("{} is invalid input".format(n))
else:
    i=1
    s=0
    while(i<=n):
        print(i)
        s=s+i
        i=i+1
    else:
        print("*"*50)
        print("\t{}".format(s))