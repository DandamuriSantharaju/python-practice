#CSVReadEx1.py
import csv
with open("C:\\CSV PYTHONfiles\\Employee.csv","r") as fp:
    csrer=csv.reader(fp)
    print("="*50)
    for record in csrer:
        for val in record:
            print("{}".format(val),end="\t\t")
        print()
    print("="*50)