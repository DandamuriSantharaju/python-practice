
#AnonymousFunEx1.py
import sys
sumop=lambda a,b:a+b
subop=lambda a,b:a-b
mulop=lambda a,b:a*b
divsop=lambda a,b:a/b
fdivsop=lambda a,b:a//b
modivop=lambda a,b:a%b
powop=lambda a,b:a**b
print("-"*50)
print("\tARTHMATIC OPERATIONS")
print("-"*50)
print("\t\t1.Addition")
print("\t\t2.Substraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.ModuloDivision")
print("\t\t6.Exponentiation")
print("\t\t7.Exit")
print("-"*50)
ch=int(input("Enter ur Choice:"))
match(ch):
    case 1:
        print("Enter Two Values for Addition:")
        a,b=float(input()),float(input())
        print("\tsum({},{})={}".format(a,b,sumop(a,b)))
    case 2:
        print("Enter Two Values for Substraction:")
        a,b=float(input()),float(input())
        print("\tSub=({},{})={}".format(a,b,subop(a,b)))
    case 3:
        print("Enter Two Values for Multiplication:")
        a, b = float(input()), float(input())
        print("\tMUL=({},{})={}".format(a, b, mulop(a, b)))
    case 4:
        print("Enter Two Values for Division:")
        a,b=float(input()),float(input())
        print("\tDivision=({},{})={}".format(a,b,divsop(a,b)))
        print("\tFloorDivision=({},{})={}".format(a,b,fdivsop(a,b)))
    case 5:
        print("Enter Two Values for ModuloDivision:")
        a,b=float(input()),float(input())
        print("\tModulio Division=({},{})={}".format(a,b,modivop(a,b)))
    case 6:
        print("Enter Two Values for Exponentiation:")
        a,b=float(input()),float(input())
        print("\tPOW=({},{})={}".format(a,b,powop(a,b)))
    case 7:
        print("Thx for Using this Program")
        exit()
    case _:
        print("UR Selection is wrong --try again")