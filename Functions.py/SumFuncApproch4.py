
#SumFuncApproch4.py
def sumop():
    # Taking Input
    a=float(input("Enter First Number:"))
    b=float(input("Enter Second Number:"))
    # Doing the Process
    c=a+b
    #give the result back to fucntion call
    return a,b,c # return stmt can return Not only one value but also returns more than one value
a,b,res=sumop() # Function call with multi line --Not taking Input But returning the Resulr
print("Sum=({}+{})={}".format(a,b,res))
print("-----------(OR)---------------")
res=sumop()# Function call with single line --Not taking Input But returning the Resulr
#here res is an object of type <class, tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("-----------(OR)---------------")
print("Sum=({},{})={}".format(res[-3],res[-2],res[-1]))