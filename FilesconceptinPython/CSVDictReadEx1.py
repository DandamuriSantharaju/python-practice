#CSVDictReadEx1.py
import csv
with open("C:\\CSV PYTHONfiles\\Products.csv", "r") as fp:
    crer=csv.DictReader(fp)
    print("-"*50)
    for record in crer:
        for k,v in record.items():
            print("{}--->{}".format(k,v))
    print("-"*50)