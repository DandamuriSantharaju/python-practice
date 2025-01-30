#Program for accepting a line of Text and Find Even and Odd Length words
#DictComprehensionEx2.py
lst=input("Enter a line of Text:")
words=lst.split()
print(words)
print("-------------------------------------------------------------------------------")
Evelist={word:len(word) for word in words if (len(word)%2==0)}
print("Even List of Words=",Evelist)
Oddlist={word:len(word) for word in words if (len(word)%2!=0)}
print("Odd List=",Oddlist)
print("-"*50)
print("Even length words")
print("------------------")
for w,wl in Evelist.items():
    print("{}---->{}".format(w,wl))
print("-"*50)
print("Odd length words")
print("----------------")
for w,wl in Oddlist.items():
    print("{}---->{}".format(w,wl))