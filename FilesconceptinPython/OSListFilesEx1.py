
#OSListFilesEx1.py
import os
fileslist=os.listdir("C:\\Python program practice")
print("------------------------------------")
print(fileslist,len(fileslist))
print("------------------------------------")
for filename in fileslist:
    # if(filename.endswith(".py")):
    if(filename.startswith("Add")):
        print("\t\t{}".format(filename))













