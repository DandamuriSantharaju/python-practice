
#ArithmeticOpFunctionsEx1.py
def menu():
    print("*"*50)
    print("\t\tARTHMATIC OPERATIONS")
    print("*"*50)
    print("\t\t1.Addition")
    print("\t\t2.Subtraction")
    print("\t\t3.Multiplication")
    print("\t\t4.Division")
    print("\t\t5.Modulo Division")
    print("\t\t6.Exponentiation")
    print("\t\t7.Exit")
    print("*"*50)
def addop():
        print("Enter Two Values for Addition")
        a,b=float(input()),float(input())
        print("\t\tSUM=({},{})={}".format(a,b,a+b))
def subop():
        print("Enter Two Numbers for Subtraction")
        a,b=float(input()),float(input())
        print("\t\tSUB=({},{})={}".format(a,b,a-b))
def mulop():
    print("Enter Two Numbers for Multiplication")
    a,b=float(input()),float(input())
    print("\tMUL=({},{})={}".format(a,b,a*b))
def divop():
    print("Enter Two Numbers for Division")
    a,b=float(input()),float(input())
    print("\tDIVISION=({},{})={}".format(a,b,a/b))
    print("\tFloor Division=({},{})={}".format(a,b,a//b))
def modop():
    print("Enter Two Numbers for modulo division")
    a,b=float(input()),float(input())
    print("\tModulo Division=({},{})={}".format(a,b,a%b))
def expop():
    a,b=float(input(("Enter Base Value:"))),float(input("Enter Power value:"))
    print("\tPOW=({},{})={}".format(a,b,a**b))
#Main program
while(True):
    menu()
    ch=int(input("Enter ur Choice:"))
    match(ch):
        case 1:
            addop()
        case 2:
            subop()
        case 3:
            mulop()
        case 4:
            divop()
        case 5:
            modop()
        case 6:
            expop()
        case 7:
            print("Thanks for using program")
            break
        case _:
            print("Ur Selecton operation is Wrong --Try again")