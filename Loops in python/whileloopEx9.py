
#whileloopEx9.py
n=int(input("Enter the number:"))
if(n<=0):
    print(f"{n} is a invalid input")
else:
    i=1
    s=0
    ss=0
    while(i<=n):
        print("{}\t\t\t\t\t{}".format(i,i**2))
        s=s+i
        ss=ss+i**2
        i=i+1
    else:
        print("*"*50)
        print("\t{}\t\t\t\t\t\t\t{}".format(s,ss))
        print("*"*50)





