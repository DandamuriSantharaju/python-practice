
#Factornum perfect or not.py
def findfactors(n):
    if(n<=1):
        print("{} Invalid Input".format(n))
    else:
        lst=[]
        pr=0
        for i in range(1,(n//2)+1):
            if(n%i==0):
                lst.append(i)
                print("\t{}".format(i))
                pr=pr+i
        else:
            if(pr==n):
                 print("Here {} is PerfectNumber".format(n))
            else:
                print("Here {} is NotPerfectNumber".format(n))
#MainProgram
n=int(input("Enter the Number to find factors:"))
findfactors(n)