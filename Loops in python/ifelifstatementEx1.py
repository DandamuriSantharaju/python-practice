
#ifelifstatementEx1.py
n=int(input("Enter a digit:"))
if(n==0):
    print("\t{} is ZERO".format(n))
elif(n==1):
    print("\t{} is ONE".format(n))
elif(n==2):
    print("\t{} is TWO".format(n))
elif(n==3):
    print("\t{} is THREE".format(n))
elif(n==4):
    print("\t{} is FOURE".format(n))
elif(n==5):
    print("\t{} is FIVE".format(n))
elif(n==6):
    print("\t{} is SIX".format(n))
elif(n==7):
    print("\t{} is SEVEN".format(n))
elif(n==8):
    print("\t{} is EIGHT".format(n))
elif(n==9):
    print("\t{} is NINE".format(n))
elif(n>9):
    print("\t{} is +ve NUMBER".format(n))
elif(n in [-1,-2,-3,-4,-5,-6,-7,-8,-9]):
    print("\t{} is -ve DIGIT".format(n))
elif(n<9):
    print("\t{} is -ve NUMBER".format(n))