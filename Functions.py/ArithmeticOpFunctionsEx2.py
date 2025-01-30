
#ArithmeticOpFunctionsEx2.py
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
def readvaluop(op):
    print("Enter Two values For {}".format(op))
    a,b=float(input()),float(input())
    return a,b
def addop():
    a,b=readvaluop("Addition")
    print("\tSUM=({},{})={}".format(a,b,a+b))
def subop():
    a,b=readvaluop("Subtraction")
    print("\tSUB=({},{})={}".format(a,b,a-b))
def mulop():
    a,b=readvaluop("Multiplication")
    print("\tMUL=({},{})={}".format(a,b,a*b))
def divop():
    a,b=readvaluop("Division")
    print("\tDIV=({},{})={}".format(a,b,a/b))
    print("\tFloor DIV=({},{})={}".format(a,b,a//b))
def modop():
    a,b=readvaluop("Modulo Divsion")
    print("\tMODULE DIVISIO=({},{})={}".format(a,b,a%b))
def expop():
    a,b=float(input("Enter Base Value:")),float(input("Enter Power Value:"))
    print("\tPOW=({},{})={}".format(a,b,a**b))
#Main Program
while(True):
    menu()
    ch=input("Enter ur choice:")
    if(ch.isdigit()):
        match(int(ch)):
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
    else:
        print("Ur Choice Must be Integer--try again")
