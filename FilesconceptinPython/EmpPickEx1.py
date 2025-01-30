#Program for Reading Employee Deatils and save then File by using Pickling Concpt
#EmpPickEx1.py
import pickle
with open("emp.pick","ab") as fp:
    while (True):
        print("-"*50)
        try:
            empno=int(input("Enter Employee number:"))
            empname=input("Enter Employee name:")
            empsal=float(input("Enter Employee Salary:"))
            empdig=input("Enter Employee Designation:")
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
