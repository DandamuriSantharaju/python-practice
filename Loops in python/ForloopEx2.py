#Program for generating mul Table for a Given Number
#ForloopEx2.py
n=input("Enter a Number for Generating mul Table:")
if(n.isdigit()):
    n=int(n)
    if(n==0):
        print("{} is invalid input".format(n))
    else:
        for i in range(1,3943):
            print("\t {} x {} = {}".format(n,i,n*i))
else:
    print("{} is invalid input".format(n))

























