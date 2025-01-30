#Program accepting List of Salaries and Give 50% Hike to Every Emp Sal
#MapEx1.py
def hike(sal):
    return (sal+sal*50/100)

#Main Program
print("Enter a list of salary's separated by space")
oldsal=list(map(float,input().split()))
print(oldsal)
newsal=list(map(hike,oldsal))
print("-"*50)
print("\tOLDSAL\t\tNEWSAL")
print("-"*50)
for ol,nl in zip(oldsal,newsal):
    print("\t{}\t\t{}".format(ol,nl))
print("-"*50)