#JSONFileDataIntoDictData.py
import json
try:
    with open("student.json","r") as fp:
        record=json.load(fp)
        print("---------------------------------------------")
        for key, value in record.items():
            print("{}-->{}".format(key, value))
except FileNotFoundError:
    print("Json File Does not Exist")