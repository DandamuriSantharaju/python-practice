
#WordLengthinLine2.py
line=input("Enter a line of Text:")
if(len(line)==0):
    print("Enter a Line of Text--Try again")
else:
    if(line.isspace()):
        print("Dont enter space--tryagain")
    else:
        dw={}
        words=line.split()
        for word in words:
            dw[word]=len(word)
        else:
            for w,wl in dw.items():
                print("\t{}-->{}".format(w, wl))