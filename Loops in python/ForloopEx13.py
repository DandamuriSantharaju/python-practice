
#ForloopEx13.py
n=int(input("Enter a Number for Calculate Factorial:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    f=1
    for i in range(1,n+1)[::-1]:
        print(i)
        f=i*f
    else:
        print("*" * 50)
        print("Factorial={}".format(f))
        print("*" * 50)