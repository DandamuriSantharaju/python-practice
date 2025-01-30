
#matchcaseEx1.py
import sys
print("*"*50)
print("\tArithmetic operations")
print("*"*50)
print("""\t\t1.Addition
    \t2.Substraction
    \t3.multiplication
    \t4.Division
    \t5.Module Division
    \t6.Exponentttation
    \t9.Exit""")
print("*"*50)
c=int(input(" Enter ur Choice :"))
print("*"*50)
match c:
    case 1:
        print("Enter Two Values for Addition:")
        a,b=float(input()),float(input())
        print("\t\tSUM({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter Two Values for Substaction:")
        a,b=float(input()),float(input())
        print("\t\tSUB({},{})={}".format(a,b,a-b))
    case 3:
        print("Enter Two Values for Multiplication:")
        a,b = float(input()), float(input())
        print("\t\tMUL({},{})={}".format(a, b, a * b))
    case 4:
        print("Enter Two Values for Division:")
        a,b=float(input()),float(input())
        print("\t\tMUL({},{})={}".format(a, b, a / b))
    case 5:
        print("Enter Two Values for Modulo Division:")
        a, b = float(input()), float(input())
        print("\t\tSUM({},{})={}".format(a, b, a % b))
    case 6:
        print("Enter Two Values for Exponention:")
        a, b = float(input()), float(input())
        print("\t\tSUM({},{})={}".format(a, b, a**b))
    case 7:
        print("Thx for Using this Program")
        sys.exit()
    case _:
        print("invalid Input")









