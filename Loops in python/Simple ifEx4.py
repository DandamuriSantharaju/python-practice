#Program for accepting positive numerical value wheter it is even or odd
#Simple ifEx4.py
n=int(input("Enter a numerical value :"))
if(n<=0):
    print("\tin valid input {}".format(n))
if(n%2==0):
    print("\t{} is even".format(n))
if(n%2!=0):
    print("\t{} is odd".format(n))
print("The execution completed")