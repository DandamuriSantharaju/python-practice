
#DUCKnumORnot.py
n = input("Enter a number: ")
if(len(n)==0):
    print("{} is invalid input".format(n))
else:
    if(n.isspace()):
        print("Dont enter the space---tryagain")
    else:
       Duk= "{} is a Duck Number.".format(n) if n.isdigit() and n[0] != '0' and '0' in n else "{} is not a Duck Number.".format(n)
       print(Duk)
        #     print("{} is a Duck Number.".format(n))
        # else:
        #     print("{} is not a Duck Number.".format(n))

























# if n.isdigit() and n[0] == '0' and '0' in n:
#     print("{} is a Duck Number.".format(n))
# else:
#     print("{} is not a Duck Number.".format(n))
