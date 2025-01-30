# #DynamicCSVFileEx1.py
# import csv
# noc=int(input("Enter How many columns you have printed:"))
# if(noc<=0):
#     print("\t{} is invalid input--try again".format(noc))
# else:
#     colnames=[]
#     for i in range(1,noc+1):
#         colname=input("Enter {} Column Name:".format(i))
#         colnames.append(colname)
#     else:
#         nor=int(input("Enter How many Records you have printed:"))
#         if(nor<=0):
#             print("\t{} is invalid input--try again".format(nor))
#         else:
#             records=[]
#             for rno in range(1,nor+1):
#                 print("-"*50)
#                 print("Enter {} Record Details".format(rno))
#                 print("-"*50)
#                 record=list()
#                 for recno in range(0,len(colnames)):
#                     val=input("\tEnter {} value:".format(colnames[recno]))
#                     record.append(val)
#                     print("*"*50)
#                 records.append(record)
#             else:
#                 while(True):
#                     filename=input("Enetr csv File name:")
#                     if(filename.endswith(".csv")):
#                         with open("C:\\CSV PYTHONfiles\\"+str(filename),"a") as fp:
#                             csvwr=csv.writer(fp)
#                             csvwr.writerow(colnames)
#                             csvwr.writerows(records)
#                             print("CSV File Created Dynamically--verify")
#                             break
#                     else:
#                         print("\tInvalid CSV File Extension--try again")
#
import csv
noc=int(input("Enetr How many Column names u have:"))
if(noc<=0):
    print("\t{} is Invalid input".format(noc))
else:
    columnames=[]
    for i in range(1,noc+1):
        columname=input("Enter {} column name:".format(i))
        columnames.append(columname)
    else:
        nor=int(input("Eneter How many rows u have:"))
        if(nor<=0):
            print("\t{} is Invalid input".format(nor))
        else:
            records=list()
            for rno in range(1,nor+1):
                print("-" * 50)
                print("Enter {} Record Details".format(rno))
                print("-" * 50)
                record=[]
                for recno in range(0,len(columnames)):
                    val=input("Enter {} vale".format(columnames[recno]))
                    record.append(val)
                records.append(record)
            else:
                while(True):
                    filename=input("Enter csv file name:")
                    if(filename.endswith(".csv")):
                        with open("C:\\CSV PYTHONfiles\\"+str(filename),"a") as fp:
                            cswer=csv.writer(fp)
                            cswer.writerow(columnames)
                            cswer.writerows(records)
                            print("csv file created Dynamicaly--varify")
                            break
                    else:
                        print("\tInvalid CSV File Extension--try again")
