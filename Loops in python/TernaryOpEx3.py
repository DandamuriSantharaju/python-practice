#Program for Accepting Two Numerical values and Find Smallest among them and check for equality.
#TernaryOpEx3.py
a,b=float(input("Enter value of a:")),float(input("Enter value of b:"))
Sml=a if a<b else b if b<a else "BOTH VALUES ARE EQUAL"
print(f"\tSmall({a},{b})={Sml}")










