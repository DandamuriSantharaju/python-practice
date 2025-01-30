
#OSremovefile.py
import os
try:
    os.remove("santha\\raju.py")
    print("File Name removed Sucessfully")
except FileNotFoundError:
    print("File does not exist")
except OSError:
    print("rmdir() can remove those folder which are empty--check ur path")