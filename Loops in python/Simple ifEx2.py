#Program for accepting Numerical Value and find smallest among them anc check for equality
#Simple ifEx2.py
a=float(input("Enter the first Numerical Number : "))
b=float(input("Enter the second Numerical Number : "))
if(a<b):
    print("\tsmall number is ({},{})={}".format(a,b,a))
if(b<a):
    print("\tsmall number is ({},{})={}".format(a,b,b))
if(a==b):
    print("\tsmall number is ({},{})={}".format(a,b,"BOTH VALUES ARE EQUAL"))
print("The execution is completed")