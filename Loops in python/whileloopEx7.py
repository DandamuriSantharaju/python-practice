
#whileloopEx7.py
n=int(input("Enter a Number for Generating Mul Table:"))
if(n==0):
    print("{} is invalid input".format(n))
else:
    i=1
    while(i<=10):
        print("{}*{}={}".format(n,i,n*i))
        i=i+1




