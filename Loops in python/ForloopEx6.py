
#ForloopEx6.py
n=int(input("Enetr How many odd numbers u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("-" * 50)
    print("List of odd numbers  order with in {}".format(n))
    print("-" * 50)
    for i in range(1,n+1,2):
        print(i)