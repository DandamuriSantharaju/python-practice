#Program for Reading Employee Details and save then File by using Pickling Concpt
#EmpPickEx1.py
import pickle,sys
class InvalidNameError(Exception):pass
class SpaceError(Exception):pass
class ZeroLengthError(Exception):pass
def validate(name:str):
    if(len(name)==0):
        raise  ZeroLengthError
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
def saveempdata():
    with open("emp.pick","ab") as fp:
        while (True):
            try:
                print("-" * 50)
                empno=int(input("Enter Employee number:"))
                empname=validate(input("Enter Employee name:"))
                empsal=float(input("Enter Employee Salary:"))
                empdig=validate(input("Enter Employee Designation:"))
                print("-"*50)
                lst=[]
                lst.append(empno)
                lst.append(empname)
                lst.append(empsal)
                lst.append(empdig)
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
# import pickle,sys
# #Programmere-Defined Exceptions
# class InvalidNameError(Exception):pass
# class SpaceError(Exception):pass
# class ZeroLengthNameError(Exception):pass
# # Hitting the Programmere-Defined Exceptions
# def validate(name:str): #name=123Guido Van Rossum
#     if(len(name)==0):
#         raise ZeroLengthNameError
#     elif(name.isspace()):
#         raise SpaceError
#     else:
#         words=name.split() # words=['123Guido','Van','Rossum']
#         res=True
#         for word in words:
#             if(not word.isalpha()):
#                 res=False
#                 break
#         if(res):
#             return name
#         else:
#             raise InvalidNameError
# #We are Defining Our Function for  Handling the Exceptions.
# def saveempdata():
#     with open("emp.pick","ab") as fp:
#         while(True):
#             try:
#                 print("-"*50)
#                 #get Emp details from KBD
#                 empno=int(input("Enter Employee Number:"))
#                 empname=validate(input("Enter Employee Name:"))
#                 empsal=float(input("Enter Employee Salary:"))
#                 empdsg=validate(input("Enter Employee Designation:"))
#                 print("-"*50)
#                 #create an empty list and the place the above values
#                 lst=[]
#                 lst.append(empno)
#                 lst.append(empname)
#                 lst.append(empsal)
#                 lst.append(empdsg)
#                 #dump the object in the file as Record
#                 pickle.dump(lst,fp)
#                 print("Emp Record Saved in a File")
#                 print("-" * 50)
#                 ch=input("Do u want to enter another record(yes/no):")
#                 if(ch.lower()=="no"):
#                     print("Thx for this program")
#                     break
#             except ValueError:
#                 print("\tDon't enter alnums,strs and symbols for Empno and salary")
#             except InvalidNameError:
#                 print("\tInvalid Emp Name / Designation--try again")
#             except SpaceError:
#                 print("\tDon't Give Space for Emp Name / Designation--try again")
#             except ZeroLengthNameError:
#                 print("\tU Must Enter Ur Name / Designation--try again")
# #Main Program
# saveempdata() # Function Call











