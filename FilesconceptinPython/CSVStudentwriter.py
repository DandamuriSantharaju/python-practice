#CSVStudentwriter.py
import csv
hname=["Rno","SNAME","MARKS"]
record=[[8,"Raju",6.94],[24,"SaiKumarRaju",6.73],[5,"john",7.56],[6,"Rosumm",89.23],
        [7,"sai",6.43]]
with open("C:\\CSV PYTHONfiles\\studen.csv","a") as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(hname)
    csvwr.writerows(record)
    print("CSV File Created-----Verify")