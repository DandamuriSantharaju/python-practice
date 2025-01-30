#Program for Accepting a Word and Decide whether It is Vowel Or Not
#BreakEx5.py
word=input("Enter a Word:")
if(len(word)==0):
    print("Word should not be empty-try again")
else:
    if(word.isspace()):
        print("Dont enyer tne space ---try again")
    else:
        res="NOT VOEEL WORD"
        for ch in word:
            if ch.lower() in ["a","e","i","o","u"]:
                res="Vowel"
                break
        print("{} is {}".format(word,res))
print("Other statements ")





# n=int(input("Enter How many values u have:"))
# if(n<=0):
#     print("{} is invalid input".format(n))
# else:
#     lst=[]
#     for v in range(1, n+1):
#         lst.append(input("Enter {} words:".format(v)))
#     else:
#         print(lst)
#         # Logic for Obtaining Unique Values
#         plist=list()
#         for v in lst:
#             if v==v[::-1]:
#                 plist.append(v)
#             else:
#                 print(plist)
#

