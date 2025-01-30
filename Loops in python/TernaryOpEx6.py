#Program for Accepting a numerical integer value and decide wheter it tis even are odd
#TernaryOpEx6.py
value=int(input("Enter a integer value :"))
# num="even" if value%2==0 else "odd"
n="{} is invalid input".format(value) if value<=0 else "{} Even".format(value) if value%2==0 else "{} is odd".format(value)
# print("\t{} is {}".format(value,num))
print(n)