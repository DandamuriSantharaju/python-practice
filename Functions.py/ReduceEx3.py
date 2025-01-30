
#ReduceEx3.py
import functools
lst=list(map(str,input("Enter List of Word separated by comma:").split(',')))
print(lst)
singword=functools.reduce(lambda x,y:x+" "+y,lst)
print(singword)
