
#ListComprehensionEx1.py
lst=[10,75,-5,64,2,9]
print("Given List=",lst)
sqlist=[val**2 for val in lst]
print("--------------------------------------------")
print("Given Value\t\tSqure Value")
print("--------------------------------------------")
for s,r in zip(lst,sqlist):
    if(type(r)!=complex):
        print("\t{}\t\t\t{}".format(s,round(r,2)))
    else:
        print("\t{}\t\t\t{}".format(s,r))