
#OSDeleteFoldersHierarchy.py
import os
while(True):
    filename=input("Enter remove Hierarchy File Name:")
    try:
        os.removedirs(filename)
        print("Folders Hierarchy Removed Successfully-verify")
        break
    except FileNotFoundError:
        print("File Does Not Exist--try again")
    except OSError:
        print("remove those folder which are empty-Check ur path of folder names")
