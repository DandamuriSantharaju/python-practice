#Program for Demonstarting Reading the data from File
#FileReadEx2.py---readlines()
try:
    with open("stud1.data") as rp:
        filedata=rp.readlines()
        print("-"*50)
        print(filedata)
        print("-"*50)
        for data in filedata:
            print(data,end="")
        print()
        print("-"*50)
except FileNotFoundError:
    print("File Does not Exist")



