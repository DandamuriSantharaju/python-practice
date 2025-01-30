#Program for accepting List of Values and get +Ve Vals
#FilterEx1.py
def positive(val):
    if (val>0):
        return True
    else:
        return False
def negative(val):
    if(val<0):
        return True
    else:
        return False

#Main Program
lst=[10,-20,-30,40,0,-50,60,-70,12]
obj1=list(filter(positive,lst))
obj2=list(filter(negative,lst))
print("Given List is ",lst)
print("Positive elements",obj1)
print("Negative elements",obj2)









