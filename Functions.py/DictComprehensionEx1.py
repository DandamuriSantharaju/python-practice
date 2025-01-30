#Program for Finding Square and Square Root for Every Value of List
#DictComprehensionEx1.py
lst=[2,4,-8,96,14,-45,36,10]
print("Given List=",lst)
sqlist={val:val**2 for val in lst} # Dict Comprehension
print("Squre List=",sqlist)
print("-----------------------------------------------------------")
print("Given Value\t\tSqure")
print("-----------------------------------------------------------")
for gv,sv in sqlist.items():
    print("\t{}\t\t\t{}".format(gv,sv))
print("-----------------------------------------------------------")
sqrlist={val:val**0.5  for val in lst} # Dict Comprehension
print("Squre Root Value=",sqrlist)
print("-----------------------------------------------------------")
print("Given value\t\tSqure root value")
print("-----------------------------------------------------------")
for gv,sr in sqrlist.items():
    if(type(sr)!=complex):
         print("\t{}\t\t\t{}".format(gv,round(sr,2)))
    else:
        print("\t{}\t\t\t{}".format(gv,sr))