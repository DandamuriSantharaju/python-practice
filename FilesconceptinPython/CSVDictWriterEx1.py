#CSVDictWriterEx1.py
import csv
hn=["PID","NAME","PRICE"]
record=[{"PID":100,"NAME":"Cadburry","PRICE":125.50},
        {"PID":200,"NAME":"DAIRY MILK","PRICE":250},
        {"PID":300,"NAME":"KIT KAT","PRICE":80},
        {"PID":400,"NAME":"kinderJoy","PRICE":100.65}]
with open("C:\\CSV PYTHONfiles\\Products.csv", "a") as fp:
    cswr=csv.DictWriter(fp,fieldnames=hn)
    cswr.writeheader()
    cswr.writerows(record)
    print("CSV File Created-----Verify")