
#ReduceEx2.py
import functools
def sumop(x,y):
    return x+y

#Main Program
lst=list(map(float,input("Enter List of elements Separated by Space:").split()))
print("Given List is ",lst)
res=functools.reduce(sumop,lst)
print("Sum of List={}".format(round(res,2)))