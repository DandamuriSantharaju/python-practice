
#StudentMarksReprtEx1.py
while(True):
    while(True):
        sno=input("Enter Student number(100-200):")
        if (sno.isdigit()) and (int(sno)) in range(100,201):
            break
        else:
            print("\t{} is Invalid Student Number--try again".format(sno))
    while(True):
        sname=input("Enter a student name:")
        words=sname.split()
        nv=True
        for word in words:
            if(not word.isalpha()):
                nv=False
                break
        if(nv):
            break
        else:
            print("\t{} is Invalid Student Name--try again".format(sno))
    while(True):
        cm=input("Enter C lang marks(0-40):")
        if (cm.isdigit()) and (int(cm)) in range(0,101):
            break
        else:
            print("\t{} is Invalid C lang marks--try again".format(sno))
    while(True):
        cppm=input("Enter C++ lang marks(0-100):")
        if (cppm.isdigit()) and (int(cppm)) in range(0,101):
            break
        else:
            print("\t{} is Invalid C++ marks--try again".format(sno))
    while(True):
        pym=input("Enter the PYTHON marks:")
        if(pym.isdigit()) and (int(pym)) in range(0,101):
            break
        else:
            print("\t{} is Invalid Python marks--try again".format(sno))
    totalmarks=int(cm)+int(cppm)+int(pym)
    percent=(totalmarks/300)*100
    if int(cm)<40 or int(cppm)<40 or int(pym)<40:
        grade="FAIL"
    else:
        if int(cm) in range(75,101):
            grade="DISTINCTION"
        elif int(cppm) in range(60,75):
            grade="FIRST"
        elif int(cppm) in range(50,59):
            grade="SECOND"
        elif (40<=int(pym)<=49):
            grade="THIRD"
    print("---------------------------------------------------")
    print("\tSTUDENT MARKS REPORT")
    print("---------------------------------------------------")
    print("\tSTUDENT NUMBER:{}".format(sno))
    print("\tSTUDENT NAME:{}".format(sname))
    print("\tSTUDENT C MARKS:{}".format(cm))
    print("\tSTUDENT C++ MARKS:".format(cppm))
    print("\tSTUDENT PYTHON MARKS:".format(pym))
    print("\tSTUDENT TOTAL MARKS in C:{}".format(totalmarks))
    print("\tSTUDENT Percentage of MARKS in :{}".format(percent))
    print("\tSTUDENT GRADE:{}".format(grade))
    print("-------------------------------------------------------")
    ch = input("Do u want to Enter Another Student Data(yes/no):")
    if(ch.lower()=="no"):
        print("Thx for Using Program")
        break