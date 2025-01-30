# Program for Generating n to 1 where n is Possitive
#WhileloopEx2.py
n=input("Ennter a +ve digit :")
if(n.isdigit()):
    num=int(n)
    if(num==0):
        print("invalid input")
    else:
        s=num
        while(s>=1):
            print(s)
            s=s-1
else:
    print("{} is invalid input".format(n))