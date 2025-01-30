#Program for Displaying OR Reading  the Content of any File
#FileReadEx3.py---read()
try:
    filename=input("Enter the file name:")
    with open(filename,"r") as rp:
        filedata=rp.readlines()
        print("-"*50)
        for data in filedata:
            print(data,end="")
        print()
        print("-"*50)
except FileNotFoundError:
    print("File Does Not Exist")