
#WordLengthinLineEx1.py
n=input("enter the any value:")
if(len(n)==0):
    print("{} is invalid input".format(n))
else:
    if(n.isspace()):
        print("{} is invalid input".format(n))
    else:
        words=n.split()
        print("Given line ={}".format(n))
        for word in words:
            print("\t\t{}--->{}".format(word, len(word)))












