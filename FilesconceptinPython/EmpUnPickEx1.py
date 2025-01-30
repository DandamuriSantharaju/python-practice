#Program for Reading Employee Records from Employee File (emp.pick)
#EmpUnPickEx1.py
import pickle
with open("emp.pick","rb") as fp:
    print("------------------------------------------")
    print("List of Employee Records")
    print("------------------------------------------")
    while(True):
        try:
            records=pickle.load(fp)
            for val in records:
                print(val,end="\t\t")
            print()
        except EOFError:
            print("----------------------------------")
            break