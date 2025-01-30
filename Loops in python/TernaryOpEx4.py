#Program for Accepting Three Numerical values and Find Biggest among them and check for equality.
#TernaryOpEx4.py
a,b,c=float(input("Enter value of a:")),float(input("Enter value of b:")),float(input("Enter value of c:"))
Big=a if a>=b and a>c else b if b>a and b>=c else c if c>=a and c>b else "ALL VALUES ARE EQUAL"
print("\tBIG({},{},{})={}".format(a,b,c,Big))
