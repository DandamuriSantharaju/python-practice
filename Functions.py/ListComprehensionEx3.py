#Program for Finding List of +Ve and -Ve Values from List of Values
#ListComprehensionEx3.py
lst=[25,0,89,78,63,-78,2.6,-74.3,1,-95]
print("Given List=",lst)
print("-------------------------------------------")
polist=[val for val in lst if val>0]
print("Positive List=",polist)
nglist=[val for val in lst if val<0]
print("Negative List=",nglist)
print("-------------------------------------------")