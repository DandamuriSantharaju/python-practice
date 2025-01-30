
#PureVarLenArgsEx3.py
def disp(sno,sname,*hyd):
    print("---------------------------------------------------")
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    print("--------------------------------------------------")
    s=0
    for val in hyd:
        print("\t{}".format(val))
        s=s+val
    else:
        print("\tSum={}".format(s))
    print("-------------------------------------------------")
#Main Program
disp(100,"Raju",10,20,30,40,50)
disp(200,"Varam",10,20,30,40)
disp(300,"sai",10,20,30)
disp(400,"Prashant",10,20)
disp(500,"Rossum",10)
disp(600,"Jhon")