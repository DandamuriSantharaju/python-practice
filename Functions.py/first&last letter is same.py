
#first&last letter is same.py
def firstandlastletter(line):
    if(len(line)==0):
        print("Enter Line of Text and it should Have words--tryagain")
    elif(line.isspace()):
        print("Line should't be empty--tryagain")
    else:
        print("---------------------------------------------")
        print("Given Line of Text")
        print(line)
        print("---------------------------------------------")
        words=line.split()
        for word in words:
            if(word[0]==word[-1]):
                print("\t{}---->is First and Last word is same".format(word))
                print("----------------------------------------")
            else:
                print("\t{}---->is First and Last word are notsame".format(word))
#MainProgram
line=input("Enter a line of text:")
firstandlastletter(line)
