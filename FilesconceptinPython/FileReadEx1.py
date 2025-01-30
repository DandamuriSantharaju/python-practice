#Program for Demonstarting Reading the data from File
#FileReadEx1.py---read()
try:
    with open("stud1.data","r") as rp:
        filedata=rp.read() # Here filedata is type type str
        print("-"*50)
        print(filedata)
        print("-"*50)
except FileNotFoundError:
    print("File does not sxist")















