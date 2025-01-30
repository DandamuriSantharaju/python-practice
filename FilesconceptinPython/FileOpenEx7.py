#Program for Opening the File in Write Mode
#FileOpenEx6.py
try:
    with open("FileOpenEx8.py","x+") as fp:
        print("---------------------------------")
        print("")
        print("File opened and created successfully")
        print("Type of fp=", type(fp))
        print("---------------------------------------")
        print("File Properties")
        print("\tFile Name=",fp.name)
        print("\tFile Mode=",fp.mode)
        print("\tIs File Reda bile=",fp.readable())
        print("\tIs file Writable=",fp.writable())
        print("\tIs File Closed=",fp.closed)
        print("---------------------------------------")
    print("Out-off with open() as Indentation")
    print("Is File Closed=",fp.closed)
except FileExistsError:
    print("File Is Arledy Existed---try again new file name")