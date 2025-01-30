
#ForloopEx4.py
n=int(input("Enetr How many numbers u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    for i in range(1,n+1)[::-1]:
        print(i)