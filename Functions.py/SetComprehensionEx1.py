#Program for Finding List of +Ve and -Ve Values from List of Values
#SetComprehensionEx1.py
lst=[10,10,50,-7,89,2.,0-89,-42,-13,6,58,83]
print("Given List=",lst)
pslist={val for val in lst if val>0}
print("Positive List=",pslist)
nglist={val for val in lst if val<0}
print("Nagative List=",nglist)
