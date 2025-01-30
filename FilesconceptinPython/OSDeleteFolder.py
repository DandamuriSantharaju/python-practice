#Program for Removing Folder / Directory
#OSDeleteFolder.py
import os
while(True):
    filename=input("Enter Delete File Name:")
    try:
        os.rmdir(filename)
        print("Folder Deleted--verify")
        break
    except FileNotFoundError:
        print("File Does not exist--try again")
    except OSError:
        print("rmdir() can remove those folder which are empty--check ur path")
