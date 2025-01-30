#OSCreateFolder.py
import os
try:
    os.mkdir("python")
    print("Folder Created--verify")
except FileExistsError:
    print("file already exist")
except FileNotFoundError:
    print("file does not exist--try again")