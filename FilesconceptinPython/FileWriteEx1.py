#Program for writing the Data to the file
#FileWriteEx1.py
sno=8
sname="Raju"
sal=17.8
with open("stud1.data","a") as fp:
    fp.write(str(sno)+" "+"\n")
    fp.write(sname+" "+"\n")
    fp.write(str(sal)+" "+"\n")
    print("Data Writen to the file--verify")