#Program for Creating Folders Herarchy
#OSCreateFoldersHierarchy.py
import os
while(True):
    try:
        foldername=input("Enter Folder name:")
        os.makedirs(foldername)
        print("Folder Crerated--verify")
        break
    except FileExistsError:
        print("Folder already Exist--try again another name")
    except FileNotFoundError:
        print("File Does not Exist--try agan")