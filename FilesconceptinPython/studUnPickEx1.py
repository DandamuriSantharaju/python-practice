
#studUnPickEx1.py
import pickle
def readmode():
    with open("stud.data","rb") as fp:
        print("-------------------------------------------")
        print("List of Employee Records")
        print("----------------------------------")
        while True:
            try:
                recods=pickle.load(fp)
                for val in recods:
                    print(val,end="\t\t")
                print()
            except EOFError:
                print("----------------------------------")
                break