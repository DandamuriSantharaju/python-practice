#EmpUpdate.py
import pickle
from symtable import Class

class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthNameError(Exception):pass
def validate(name:str): #name=123Guido Van Rossum
    if(len(name)==0):
        raise ZeroLengthNameError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split() # words=['123Guido','Van','Rossum']
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            return name
        else:
            raise InvalidNameError
def updateemp():
    with open("employee.data","rb") as fp:
        try:
            empno=int(input("Enter Employee Number to update emp name and sal:"))
            empname=validate(input("Enter Employee name:"))
            empsal=float(input("Enter Employee Salary:"))
            emplist=[]
            while(True):
                try:
                    record=pickle.load(fp)
                    emplist.append(record)
                except EOFError:
                    break
            res=False
            for ind in range(len(emplist)):
                if(emplist[ind][0]==empno):
                    index=ind
                    res=True
                    break
            if(res):
                emplist[index][1]=empname
                emplist[index][2]=empsal
                print("Employee Data Updated-Verify")
                with open("employee.data","wb") as fp:
                    for record in emplist:
                        pickle.dump(record,fp)
                    print("\tEmployee Data Updated-Verify")
            else:
                print("\tEmployee number does not exist-can't update")
        except ValueError:
            print("\tDon't enter alnums,strs and symbols for Choice-try again")
        except InvalidNameError:
            print("\tInvalid Emp Name / Designation--try again")
        except SpaceError:
            print("\tDon't Give Space for Emp Name / Designation--try again")
        except ZeroLengthNameError:
            print("\tU Must Enter Ur Name / Designation--try again")

