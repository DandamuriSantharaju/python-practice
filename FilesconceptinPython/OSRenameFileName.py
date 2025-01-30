
#OSRenameFileName.py
import os
try:
    os.rename("C:\\RAJU\\AP\\WESTGOD\\TPG","C:\\RAJU\\AP\\WESTGOD\\TPG")
    print("File name modified--verify")
except FileExistsError:
    print("Folder already Exist--try again another name")
except FileNotFoundError:
    print("File Does not Exist--try again")
except OSError:
    print("The parameter is incorrect")