
#MapEx6.py
print("Enter a list of numbers separated by space")
val=list(map(float,input().split()))
cubval=list(map(lambda cb:cb**3,val))
print("-"*50)
print("\tvalue\t\tCubes value")
print("-"*50)
for gv,cbv in zip(val,cubval):
    print("\t{}\t\t{}".format(gv,cbv))
print("-"*50)