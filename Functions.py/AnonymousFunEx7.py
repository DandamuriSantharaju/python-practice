
#AnonymousFunEx7.py
smallest = lambda a, b, c: a if a < b and a < c else b if b < c else c

equal1 = lambda a, b, c: a == b and a != c
equal2 = lambda a, b, c: b == c and a != b
equal3 = lambda a, b, c: a == c and a != b
equal4 = lambda a, b, c: a == b == c

# Main Program
print("Enter three values")
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))
c = float(input("Enter third value: "))
# a,b,c=float(input()),float(input()),float(input())
small = smallest(a, b, c)
print(f"The smallest number is: {small}")

if equal1(a, b, c):
    print("a and b values are equal.")
elif equal2(a, b, c):
    print("b and c values are equal.")
elif equal3(a, b, c):
    print("a and c values are equal.")
elif equal4(a, b, c):
    print("All three values are equal.")
else:
    print("The numbers are not all equal.")