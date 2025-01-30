

#NameValidationEx1.py
name=input("Enter Your Name:")
print("Given Name is : {}".format(name))
words=name.split()
nv=True
for word in words:
    if not word.isalpha():
        nv = False
        break
if(nv):
    print("{} valid name".format(name))
else:
    print("{} is invalid name".format(name))
