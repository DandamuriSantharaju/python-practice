
#ForloopEx8.py
n=int(input("Enetr How many even numbers u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-"*50)
    print("List of even numbers reverse order with in {}".format(n))
    print("-"*50)
    for i in range(1,n+1,2)[::-1]:
        print(i)