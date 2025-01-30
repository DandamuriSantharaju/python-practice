
#Magicnum or not.py
n = input("Enter a number: ")
if(len(n)==0):
    print("{} is invalid input".format(n))
else:
    if(n.isspace()):
        print("Dont enter the space---tryagain")
    else:
        # s=int(n)*int(n)
        # x=str(n)
        # z=str(s)
        mag="{} is a magic Number.".format(n) if str(int(n)*int(n)).endswith(n) else "{} is not a magic Number.".format(n)
        print(mag)
        # if z.endswith(x):
        #     print("{} is a magic Number.".format(n))
        # else:
        #     print("{} is not a magic Number.".format(n))
