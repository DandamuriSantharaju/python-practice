#Program for accepting List of Values and get +Ve Vals
#FilterEx3.py
positive= lambda val: val>0
negative= lambda val: val<0

#Main Program
print("Enter Elements Separated by Space")
lst=[float(val) for val in input().split()]

pslist=list(filter(positive,lst))
nglist=tuple(filter(negative,lst))

print("Given Elements=",lst)
print("Positive Elements=",pslist)
print("Negative Elements=",nglist)
