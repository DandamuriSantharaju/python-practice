
#FilterEx4.py
print("Enter List of Elements separated by space")
lst=[float(val) for val in input().split()]
pslist=list(filter(lambda val: val>0,lst))
nglist=tuple(filter(lambda val: val<0,lst))
print("Given elements=",lst)
print("Positive Elements=",pslist)
print("Negative elements=",nglist)