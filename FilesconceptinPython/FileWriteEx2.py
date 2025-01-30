#Program for writing the Data to the file
#FileWriteEx2.py
while(True):
    print("-"*50)
    eno=int(input("Enter a Employe number:"))
    ename=input("Enter a name:")
    sal=float(input("Enetr emp sal:"))
    print("-"*50)
    with open("stud1.data","a+") as fp:
        fp.write(str(eno)+"\t")
        fp.write(ename+"\t")
        fp.write(str(sal)+"\n")
        print("Data Written to the File--Verify")
        print("-" * 50)
        ch = input("Do u want to Insert another record(yes/no):")
        if (ch.lower() == "no"):
            print("Thx for using this program")
            break