#write a python program which will gererat prime numbers with given range n
#InnerLoopEx9.py
n=int(input("Enter the How many Range values primes will de displayed:"))
if(n<=1):
    print("Invalid input")
else:
    print("-"*50)
    print("The first {} prime numbers are".format(n))
    print("-"*50)
    prime=0
    num=2
    while prime <n:
        res=True
        for i in range(2,int(num *0.5) + 1):
            if num%i==0:
                res=False
                break
        if res:
            print("\t\t",num)
            prime +=1
        num +=1
print("-"*50)