
#ReduceEx1.py
import functools
lst=list(map(float,input("Enter List of values separated by space:").split()))
print("Given List ",lst)
sumop=functools.reduce(lambda x,y:x+y,lst)
print("sum of list={}".format(sumop))