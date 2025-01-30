#Program for accepting a Line of Text and place reverse of every word in same place of Line
#WordReverseInLine.py
line=input("Enter a linr=e of text:")
if(len(line)==0):
    print("Enter a line of Text -- tryagain")
else:
    if(line.isspace()):
        print("Dont enter the space -- tryagain")
    else:
        print("----------------------------")
        print("Given Line={}".format(line))
        words=line.split()
        rew=[]
        for word in words:
            rew.append(word[::-1])
        else:
            print("Reversed line with Words={}".format(" ".join(rew)))
            print("----------------------------")







# line=input("Enter a Line of Text:")
# if(len(line)==0):
#     print("Enter a Line of Text--Try again")
# else:
#     if(line.isspace()):
#         print("Dont enter space--try again:")
#     else:
#         print("----------------------------")
#         print("Given Line={}".format(line))
#         words=line.split()
#         rwl=[]
#         for word in words:
#             rwl.append(word[::-1])
#         else:
#             print("Reversed line with Words={}".format(" ".join(rwl)))
#             print("----------------------------")