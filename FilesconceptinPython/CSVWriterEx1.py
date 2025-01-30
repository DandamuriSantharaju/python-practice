
#CSVWriterEx1.py
import csv

hname=["Eno","Ename","Sal"]
records=[[100,"Raju",456.12],
         [200,"varam",983.78],
         [300,"siva",789.46],
         [400,"sai",861.2],
         [500,"pra",963.15],
         [600,"johan",231.45]]
with open("C:\\CSV PYTHONfiles\\Employee.csv","a") as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(hname)
    csvwr.writerows(records)
    print("CSV File Created-----Verify")