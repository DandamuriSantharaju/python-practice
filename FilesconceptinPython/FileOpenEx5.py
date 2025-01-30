#Program for Opening the File in Write Mode
#FileOpenEx5.py
try:
    with open("stud1.data","r+") as fp:
        print("-------------------------------------")
        print("File opened and created successfully")
        print("Type of fp=",type(fp))
        print("---------------------------------------")
        print("File properties")
        print("\tIs File closed=", fp.closed)
        print("\tFile Name=", fp.name)
        print("\tFile Mode=", fp.mode)
        print("\tIs File Redabile=", fp.readable())
        print("\tIs File Writebile=", fp.writable())
    print("---------------------------------------------")
    print("Out-off with open() as Indentation")
    print("File Is closed={}".format(fp.closed))
except FileNotFoundError:
    print("File Does Not Exist")
