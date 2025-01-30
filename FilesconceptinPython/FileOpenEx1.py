#Program for Opening the File in Read Mode
#FileOpenEx1.py
try:
    fp=open("stud1.data","r")
except FileNotFoundError:
    print("File Does Not Exist")
else:
    print("--------------------------")
    print("I am else Part")
    print("File Opened in Read Mode Successfully")
    print("Type of fp=",type(fp))
    print("IS file colsed",fp.closed)
finally:
    try:
        print("-------------------------")
        fp.close()
        print("Thx for using this file")
        print("File Closed Successfully")
        print("IS file colsed",fp.closed)
        print("-------------------------")
    except NameError:
        print("File Not at all Opened in Read Mode--No need to close")













