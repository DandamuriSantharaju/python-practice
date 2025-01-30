#EmpSearch.py
import pickle
def searchemp():
    try:
        empno=int(input("Enter Employee number:"))
        emplist=[]
        with open("employee.data","rb") as fp:
            while(True):
                try:
                    record=pickle.load(fp)
                    emplist.append(record)
                except EOFError:
                    break
            res=False
            for val in emplist:
                if(val[0]==empno):
                    res=True
                    rec=val
                res=True
            if(res):
                print("\t{} Employee Number  Exist".format(empno))
            else:
                print("\t{} Employee Number Does not Exist".format(empno))
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice-try again")
