

#StudentMarksReprtEx1.py
while(True):
    sno=input("Enter Student number(100-200):")
    if(sno.isdigit()) and (int(sno)) in range(100,201):
        break
    else:
        print("\t{} is Invalid Student Number--try again".format(sno))
while(True):
    sname=input("Enter student name:")
    words=sname.split()
    nv=True
    for word in words:
        if(not word.isalpha()):
            nv=False
            break
    if(nv):
        break
    else:
        print("\t{} is Invalid Student Number--try again".format(sname))
while(True):
    CM=input("Enter C lang marks:")
    if (CM.isdigit()) and (int(CM)) and (0<=int(CM)<=100):
        break
    else:
        print("\t{} is Invalid C Marks--try again".format(sno))
while(True):
    CPPM=input("Enter C++ lang Marks:")
    if (CPPM.isdigit()) and (int(CPPM)) and (0<=int(CPPM)<=100):
        break
    else:
        print("\t{} is Invalid C++ Marks--try again".format(sno))
while(True):
    PYM=input("Enter PYM lang Marks:")
    if (PYM.isdigit()) and (int(PYM)) and (0<=int(PYM)<=100):
        break
    else:
        print("\t{} is Invalid PYTHON Marks--try again".format(sno))
totalmarks=int(CM)+int(CPPM)+int(PYM)
percentage=(totalmarks/300)*100
if (int(CM)<40) or (int(CPPM)<40) or (int(PYM)<40):
     grade="Fail"
else:
     if(percentage in range(75,101)):
         grade="DISTINCTION"
     elif(percentage in range(60,75)):
         grade="FIRST"
     elif(50<=percentage<=59):
         grade="SECIOND"
     elif(40<=percentage<=49):
         grade="THIRD"
print("*"*50)
print("\tSTUDENT MARKS REPORT")
print("*"*50)
print("\tSTUDENT NUMBER:{}".format(sno))
print("\tSTUDENT NAME:{}".format(sname))
print("\tSTUDENT MARKS in C:{}".format(CM))
print("\tSTUDENT MARKS in C++:{}".format(CPPM))
print("\tSTUDENT MARKS in PYTHON:{}".format(PYM))
print("\tSTUDENT TOTAL MARKS in C:{}".format(totalmarks))
print("\tSTUDENT Percentage of MARKS in :{}".format(percentage))
print("\tSTUDENT GRADE:{}".format(grade))
print("*"*50)