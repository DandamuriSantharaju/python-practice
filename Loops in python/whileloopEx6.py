
#whileloopEx6.py
n=int(input("Enterv the +ve number:"))
if(n<=0):
    print(f"{n} is invalid input")
else:
    if n%2 == 0:
        n=n-1
    i=n
    while(i>=1):
        print(i)
        i=i-2