#Program for accepting List of Values and get +Ve Vals
#FilterEx2.py
def positive(val):
    if val>0:
        return True
    else:
        return False
def negative(val):
    if val<0:
        return True
    else:
        return False

#Main Program
print("Enter List of elements Seperated by space")
lst=[float(val) for val in input().split()]

pslist=list(filter(positive,lst))
nglist=tuple(filter(negative,lst))
print("Given Elements=",lst)
print("Positive Elements=",pslist)
print("Negative Elements=",nglist)


