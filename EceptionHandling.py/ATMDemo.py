
#ATMDemo.py
from ATMMenu import menu
from ATMOperations import deposite,withdraw,Balenq
from ATMException import DepositEroor,WithdrawEroor,InsuffFoundError
while(True):
    menu()
    try:
        ch=int(input("Enter ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposite()
                except ValueError:
                    print("\tDont try to alnums,strs and symbols--try again")
                except DepositEroor:
                    print("\tDon't try to Deposit -ve or zerro value--try again")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("\tDont try to alnums,strs and symbols--try again")
                except WithdrawEroor:
                    print("\tDon't try to Deposit -ve or zerro value--try again")
                except InsuffFoundError:
                    print("\tU don't have sufficent Funds--try again")
            case 3:
                Balenq()
            case 4:
                print("\t Thanks For Using This Program")
                break
            case _:
                print("\t UR Selection Of Operation is Wrong--try again")
    except ValueError:
        print("\tDont try to alnums,strs and symbols--try again")
