#Program for Finding Square of Every Element of List
#TupleComprehensionEx1.py
lst=(12,4,15,8,-5,0,17)
print("Given Tuple=",lst)
sqlist=(val*2 for val in lst)
print(sqlist)
sqlelements=tuple(sqlist)
print(sqlelements)
print("-------------------------------------------------------------------")
print("Given Value\t\tSqure Value")
print("-------------------------------------------------------------------")
for gv,sv in zip(lst,sqlelements):
    if (type(sv)!=complex):
        print("\t{}\t\t\t{}".format(gv,round(sv,2)))
    else:
        print("\t{}\t\t\t{}".format(gv,sv))