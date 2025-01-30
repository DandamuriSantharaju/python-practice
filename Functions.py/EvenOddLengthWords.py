
#EvenOddLengthWords.py
def findwordlength(line):
    if(len(line)==0):
        print("Enter Line of Text and It should Have words--tryagain")
    elif(line.isspace()):
        print("Line should't be empty--try again")
    else:
        odddict={}
        evendict={}
        words=line.split()
        for word in words:
            if(len(word)%2==0):
                evendict[word]=len(word)
            else:
                odddict[word]=len(word)
        else:
            print("Even words and their length")
            for w,l in evendict.items():
                print("\t----->{}".format(w,l))
            print("-----------------------------------")
            print("odd words and their length")
            for w,l in odddict.items():
                print("\t{}-------->{}".format(w,l))
            print("=================OR========================")
            print("Even Wrods and their Length")
            for w1 in evendict.items():
                print("\t{}----->{}".format(w1[0],w1[1]))
            print("======================OR=====================")
            print("odd words and their lenngth")
            for x in odddict.keys():
                print("\t{}----->{}".format(x,odddict.get((x))))

 #MainProgram
line=input("Enter line pf text:")
findwordlength(line)


