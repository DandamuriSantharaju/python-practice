
#whileloopEx11.py
n=int(input("Enter Number for Cal Factorial:"))
if(n<0):
    print("{} is a invalid input".format(n))
else:
    i=1
    p=1
    while(i<=n):
        p=p*i
        i=i+1
    else:
        print("*"*50)
        print("Factorial({})={}".format(n,p))