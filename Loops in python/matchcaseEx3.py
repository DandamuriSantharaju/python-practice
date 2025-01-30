
#matchcaseEx3.py
import sys
print("*"*50)
print("\t\tCovert the temperatures")
print("*"*50)
print("""\t\tFC.Fahrenheit to Celcius
    \tFK.Fahrenheit to Kelvin
    \tCF.Celsius to Fahrenheit
    \tCK.Celsius to Kelvi
    \tKC.Kelvin to Celcius
    \tKF.Kelvin to Fahrenheit
    \tE.Exit""")
print("*"*50)
t=input("Enter ur Choice :")
match t:
    case "FC"|"fc":
        print("Fahrenheit to Celcius")
        f=float(input("Enter a Fahrenheit temperatures :"))
        print("\t\tFahrenheit is {} to Celcius is {}".format(f,(f-32)*(5/9)))
    case "FK" | "fk":
        print("Fahrenheit to kelvin")
        f = float(input("Enter a Fahrenhei temperatures :"))
        print("\t\tFahrenheit is {} to Kelvin is {}".format(f, (f - 32) * (5 / 9)+273.15))
    case "CF" | "cf":
        print("Celsius to Fahrenheit")
        c = float(input("Enter a Celsiusi temperatures :"))
        print("\t\tCelcius is {} to Fahrenhei is {}".format(c, (c*(9/5)+32)))
    case "CK" | "ck":
        print("Celsius to Kelvin")
        c = float(input("Enter a Celsius temperatures :"))
        print("\t\tCelcius is {} to Kelvin is {}".format(c, (c+273.15)))
    case "KC" | "kc":
        print("Kelvin to Celcius")
        k = float(input("Enter a Kelvin temperatures :"))
        print("\t\t Kelvin is {} to Celcius is {}".format(k, k-273.15))
    case "KF" | "kf":
        print("Kelvin to Fahrenheit")
        k = float(input("Enter a Kelvin temperatures :"))
        print("\t\tKelvin is {} to Fahrenheit is {}".format(k, (k-273.15)*(9/5)+32))
    case "EXIT" | "exit":
        print("Thx for Using this Program")
        sys.exit()
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("Match case completed")
