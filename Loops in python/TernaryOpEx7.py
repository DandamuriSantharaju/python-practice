#program for accepting a numrical value dcide positive or negative or equal
#TernaryOpEx7.py
n=int(input("Enter a numrical value:"))
rel="Positive" if n>0 else "negative" if n<0 else "Zero"
print("\t{} is {}".format(n,rel))