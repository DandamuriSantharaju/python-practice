#Program for Copying the content of One File into Another File
#To Copy, we Need two Files--Source File   and Destination File
#Source File Must be Opened in Read Mode
#Destination File Must be Opened in Write Mode
#FileCopy.py
try:
    srcfile=input("Enter the source file:")
    with open(srcfile,"r") as sp:
        dstfile=input("Enter Destination File Name:")
        with open(dstfile,"a") as wp:
            # Read the Data from Source File
            srcdata=sp.read()
            #Write Source File Data to Destination File
            wp.write(srcdata)
            print("File Copied--verify")
except FileNotFoundError:
    print("Source File does Not Exist")