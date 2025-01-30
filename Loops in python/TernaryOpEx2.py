#Program for Accepting Two Numerical values and Find Biggest among them and check for equality.
#TernaryOpEx2.py
a,b=float(input("Enter the value of a:")),float(input("Enter the value of b:"))
BIG=a if a>b else b if b>a else "BOTH VALUES ARE EQUAL"
print("\tBIG({},{})={}".format(a,b,BIG))












