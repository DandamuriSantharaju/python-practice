#EmpView.py
import pickle
def viewemployee():
    try:
        empno=int(input("Enter Employee Number:"))
        print("-------------------------------------")
        print("\tList of Employee Records")
        print("-------------------------------------")
        emplis=[]
        with open("employee.data", "rb") as fp:
            while(True):
                try:
                    record=pickle.load(fp)
                    emplis.append(record)
                except EOFError:
                    break
            res="NotFound"
            for emprec in emplis:
                if(emprec[0]==empno):
                    res="found"
                    rec=emprec
                    break
            if(res=="found"):
                print("\tEmployee Number:{}".format(rec[0]))
                print("\tEmployee Name:{}".format(rec[1]))
                print("\tEmployee Salary:{}".format(rec[2]))
                print("-------------------------------------")
            else:
                print("\t{} Employee Number Does not Exist".format(empno))
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice-try again")




def viewallemployees():
    with open("employee.data","rb") as fp:
        print("-------------------------------------")
        print("\tList of Employee Records")
        print("-------------------------------------")
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print(val,end="\t\t")
                print()
            except EOFError:
                break