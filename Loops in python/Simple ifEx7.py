#program for display the following cource names
#Simple ifEx7.py
print("""SELECT ONE COURCE
1.C
2.C++
3.PYTHON
4.JAVA""")
n=input("Enter a cource name :")
if(n.lower()=="c"):
    print("\t{} is developed by Dennis Ritchie".format(n))
if(n.lower()=="c++"):
    print("\t{} is developed by Bjarne Stroustrup".format(n))
if(n.lower()=="python"):
    print("\t{} is developed by VAN ROSSUM".format(n))
if(n.lower()=="java"):
    print("\t{} is developed by james".format(n))
if n not in ["c","c++","python","java","C","c++","PYTHON","JAVA"]:
    print("invalid cource Name")
print("Program execution completed")















