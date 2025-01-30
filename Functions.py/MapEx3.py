
#MapEx3.py
print("Enter a list of salary's separated by space")
oldsal=list(map(float,input().split()))
newsal=list(map(lambda sal:sal+sal*50/100,oldsal))
print("-"*50)
print("\tOLDSAL\t\tNEWSAL")
print("-"*50)
for ol,nl in zip(oldsal,newsal):
    print("\t{}\t\t{}".format(ol,nl))
print("-"*50)