#Program for Calculating Sum of Two Numbers by using Functions
#SumFuncApproch1.py
def sumop(k,v):
    r=k+v
    return r
#Main Program
x=float(input("Enter First Number:"))
y=float(input("Enter Second Number:"))
res=sumop(x,y)
print("Sum({},{})={}".format(x,y,res))
print("------------------------------------")
k=float(input("Enter First Number:"))
v=float(input("Enter Second Number:"))
r=sumop(k,v)
print("Sum=({},{})={}".format(k,v,r))