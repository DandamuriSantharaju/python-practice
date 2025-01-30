#Program for Finding the Factors of a Given Number by using Functions
#FactorsEx1.py
def findfactors(n):
    if(n<=1):
        print("{} Invalid Input".format(n))
    else:
        for i in range(1,(n//2)+1):
            if(n%i==0):
                print("\t{}".format(i))
#MainProgram
n=int(input("Enter the Number to find factors:"))
findfactors(n)