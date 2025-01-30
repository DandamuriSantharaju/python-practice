
#KeywordArgsEx1.py
def disp(a,b,c,d,e):
    print("\t{}\t{}\t{}\t{}\t{}".format(a,b,c,d,e))



#main  Program
print("-"*50)
print("\tA\tB\tC\tD\tE")
print("-"*50)
disp(10,20,30,40,50)
disp(a=10,b=20,c=30,d=40,e=50)
disp(10,20,d=40,e=50,c=30)