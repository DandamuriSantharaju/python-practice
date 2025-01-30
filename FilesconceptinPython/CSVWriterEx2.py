#CSVWriterEx2.py
import csv


records=[700,"Rossum",78.56]
with open("C:\\CSV PYTHONfiles\\Employee.csv","a") as fp:
    cswer=csv.writer(fp)
    cswer.writerow(records)
    print("CSV File Created-----Verify")