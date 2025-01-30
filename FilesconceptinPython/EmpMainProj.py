#EmpMainProj.py
from EmpMenu import menu
from EmpAdd import empadd
from EmpView import viewallemployees,viewemployee
from EmpSearch import searchemp
from  EmpUpdate import updateemp
from EmpDelete import deleteemp
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                empadd()
            case 2:
                deleteemp()
            case 3:
                updateemp()
            case 4:
                viewemployee()
            case 5:
                viewallemployees()
            case 6:
                searchemp()
            case 7:
                print("Thx for using this Program")
                break
            case _:
                print("\tUr Selection is Wrong--Try again")
    except ValueError:
        print("\tDon't enter alnums,strs and symbols for Choice-try again")

