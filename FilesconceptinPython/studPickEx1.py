
#studPickEx1.py
import pickle
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthError(Exception):pass
def validt(name:str):
    if(len(name)==0):
        raise ZeroLengthError
    elif(name.isspace()):
        raise SpaceError
    else:
        words=name.split()
        res=True
        for word in words:
            if (not word.isalpha()):
                res = False
                break
            if (res):
                return name
            else:
                raise InvalidNameError
def saveempdata():
    with open("Stud.data","ab") as fp:
        while(True):
            try:
                print("-"*50)
                studno=int(input("Enter Student number:"))
                studname=validt(input("Enter Student Name:"))
                studmarks=float(input("Enter Student Marks:"))
                studcollege=validt(input("Enter College Name"))
                lst=[]
                lst.append(studno)
                lst.append(studname)
                lst.append(studmarks)
                lst.append(studcollege)
                pickle.dump(lst,fp)
                print("Emp Record save in file")
                ch = input("Do u want to enter another record(yes/no):")
                if (ch.lower() == "no"):
                    print("Thx for this program")
                    break
            except ValueError:
                print("Dont Enter the alnums in Empno and empsal")
            except InvalidNameError:
                print("\tInvalid Emp Name / Designation--try again")
            except SpaceError:
                print("\tDon't Give Space for Emp Name / Designation--try again")
            except ZeroLengthError:
                print("\tU Must Enter Ur Name / Designation--try again")
saveempdata()