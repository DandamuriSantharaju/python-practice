
#MapEx7.py
print("Enter a list of words separated by space")
val=list(map(str,filter(str.isalpha,input().split())))
print(val)
resval=list(map(lambda vals:vals[::-1],val))
print("-"*50)
print("\twoard\t\tReversewoard")
print("-"*50)
for w,res in zip(val,resval):
    print("\t{}\t\t{}".format(w,res))
print("-"*50)