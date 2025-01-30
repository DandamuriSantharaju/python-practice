
#AnonymousFunEx3.py
import sys
ctokop=lambda c:c+273.15
ktocop=lambda k:k-273.15
ftocop=lambda f:(f-32)*(5/9)
ctofop=lambda c:(c*1.8)+32
ftokop=lambda f:(f-32)*(5/9)+273.15
ktofop=lambda k:(k-273.15)*(9/5)+32
print("-"*50)
print("\t\tTEMPERATURE CONVERSATIONS")
print("-"*50)
print("\t1.Celsius to Kelvin")
print("\t2.Kelvin to Celsius")
print("\t3.Fahrenheit to Celsius")
print("\t4.Celsius to Fahrenheit")
print("\t5.Fahrenheit to Kelvin")
print("\t6.Kelvin to Fahrenheit")
print("\t7.EXIT")
print("-"*50)
ch=int(input("Enter UR choice:"))
match(ch):
    case 1:
        c=float(input("Enter Celsius Temperature:"))
        print("\tCelsius Temperature {} to Kelvin Temperature {}".format(c,ctokop(c)))
    case 2:
        k=float(input("Enter Kelvin Temperature:"))
        print("\tKelvin Temperature {} to Celsius Temperature {}".format(k,ktocop(k)))
    case 3:
        f=float(input("Enter Fahrenheit Temperature:"))
        print("\tFahrenheit Temperature {} to Celsius Temperature {}".format(f,ftocop(f)))
    case 4:
        c=float(input("Enter Celsius Temperature:"))
        print("\tcelsius Temperature {} to Fahrenheit Temperature {}".format(c,ctofop(c)))
    case 5:
        f=float(input("Enter Fahrenheit Temperature:"))
        print("\tFahrenheit Temperature {} to Kelvin Temperature {}".format(f,ftokop(f)))
    case 6:
        k=float(input("Enter Kelvin Temperature:"))
        print("\tKelvin Temperature {} to Fahrenheit Temperature {}".format(k,ktofop(k)))
    case 7:
        print("Thx for Using this Program")
        exit()
    case _:
        print("UR Selection is wrong --try again")