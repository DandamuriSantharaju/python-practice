##Program for Formula problem a^m/a^n of Arithmetic operators
#formulaProblemEx5.py
#--------------------(Logic-1)----------------------
a=float(input("Enter a number for a:"))
m=float(input("Enter a number for power m:"))
n=float(input("Enter a number for power n:"))
b=(a**m)/(a**n)
print("\t\tThe  a^m/a^n is {}".format(b))
#--------------------(Logic-2)----------------------
a=float(input("Enter a number for a:"))
m=float(input("Enter a number for power m:"))
n=float(input("Enter a number for power n:"))
b=a**(m-n)
print("\t\tThe  a^m/a^n is {}".format(b))
