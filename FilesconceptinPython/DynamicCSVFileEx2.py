#DynamicCSVFileEx2.py
# import csv
#
# noc=int(input("Enter How many column u have:"))
# if(noc<=0):
#     print("{} is invalid input".format(noc))
# else:
#     columnaes=[]
#     for i in range(1,noc+1):
#         columnae=input("Enetr {} Cloumn name:".format(i))
#         columnaes.append(columnae)
#     else:
#         nor=int(input("Enter How many rows u have:"))
#         if(nor<=0):
#             print("\t{} is invalid input".format(nor))
#         else:
#             records=list()
#             for rno in range(1,nor+1):
#                 print("-" * 50)
#                 print("Enter {} Record Details".format(rno))
#                 print("-" * 50)
#                 record={}
#                 for renco in range(0,len(columnaes)):
#                     val=input("Eneter {} value:".format(columnaes[renco]))
#                     record[columnaes[renco]]=val
#                 records.append(record)
#             else:
#                 while(True):
#                     filename=input("Enetr csv file name:")
#                     if(filename.endswith(".csv")):
#                         with open("C:\\CSV PYTHONfiles\\"+str(filename),"a") as fp:
#                             cswer=csv.DictWriter(fp,fieldnames=columnaes)
#                             cswer.writeheader()
#                             cswer.writerows(records)
#                             print("csv file created Dynamicaly--varify")
#                             break
#                     else:
#                         print("\tInvalid CSV File Extension--try again")
import csv

noc=int(input("Enetr How Many columns u have:"))
if(noc<=0):
    print("\t{} is invalid input".format(noc))
else:
    columnames=[]
    for i in range(1,noc+1):
        columname=input("Enter {} column value:".format(i))
        columnames.append(columname)
    else:
        nor=int(input("Enter How Many Rows U have:"))
        if(nor<=0):
            print("\t{} is invalid input".format(nor))
        else:
            records=list()
            for rno in range(1,nor+1):
                print("-" * 50)
                print("Enetr {} Record Details".format(rno))
                print("-" * 50)
                record={}
                for renco in range(0,len(columnames)):
                    val=input("Enetr {} value".format(columnames[renco]))
                    record[columnames[renco]]=val
                records.append(record)
            else:
                while(True):
                    filename=input("Enter csv file name:")
                    if(filename.endswith(".csv")):
                        with open("C:\\CSV PYTHONfiles\\"+str(filename),"w") as fp:
                            cswer=csv.DictWriter(fp,fieldnames=columnames)
                            cswer.writeheader()
                            cswer.writerows(records)
                            print("csv file created Dynamicaly--varify")
                            break
                    else:
                        print("\tInvalid CSV File Extension--try again")

