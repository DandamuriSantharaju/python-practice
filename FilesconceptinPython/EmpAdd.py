#EmpAdd.py
import pickle

from EmpUpdate import ZeroLengthNameError


class InvalidNameError:pass
class SpaceError:pass
class ZeroLengthNmaeError:pass
def validate(name:str):
    if(len(name)==0):
        raise ZeroLengthNameError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        res=True
        for word in words:
            if(not word.isalpha()):
                res=False
                break
        if(res):
            return name
        else:
            raise InvalidNameError
def empadd():
    with open("employee.data","ab") as fp:
        while(True):
            try:
                print("-"*50)
                empno=int(input("Enter Employee number:"))
                empname=validate(input("Enter Employee Name:"))
                empsal=float(input("Enter Employee Salary:"))
                emplist=[]
                emplist.append(empno)
                emplist.append(empname)
                emplist.append(empsal)
                pickle.dump(emplist,fp)
                print("Emp Record Saved in a File")
                print("-"*50)
                ch=input("Do u Want To Enter Another Record(yes/no):")
                if(ch.lower()=="no"):
                    print("Thx for this program")
                    break
            except ValueError:
                print("\tDon't enter alnums,strs and symbols for Choice-try again")
            except InvalidNameError:
                print("\tInvalid Emp Name / Designation--try again")
            except SpaceError:
                print("\tDon't Give Space for Emp Name / Designation--try again")
            except ZeroLengthNameError:
                print("\tU Must Enter Ur Name / Designation--try again")

