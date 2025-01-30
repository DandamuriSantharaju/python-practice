from ATMException import DepositEroor,WithdrawEroor,InsuffFoundError
bal=500.00
def deposite():
    damt=float(input("Enter Deposit Amount:"))
    if(damt<=0):
        raise DepositEroor
    else:
        global bal
        bal=bal+damt
        print("\tUr Acoount xxxxxx123 Credited with INr:{}".format(damt))
        print("\tNOW ur Account xxxxxxxx123 Balance with INR:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("Enter withdraw Amount:"))
    if (wamt <= 0):
        raise WithdrawEroor
    elif((wamt+500)>bal):
        raise InsuffFoundError
    else:
        bal = bal - wamt
        print("\tUr Acoount xxxxxx123 Debited with INr:{}".format(wamt))
        print("\tNOW ur Account xxxxxxxx123 Balance with INR:{}".format(bal))
def Balenq():
    print("\tNOW ur Account xxxxxxxx123 Balance with INR:{}".format(bal))
