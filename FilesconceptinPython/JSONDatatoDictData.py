#JSONDatatoDictData.py
import json
jsondata='{"pid":1,"pname":"laptop","price":39000.984}'
print(jsondata,type((jsondata)))
print("----------------------------------------------")
#convert JSON Data into Dict object data--we use loads() of json module
d=json.loads(jsondata)
print(d,type(d))
print("----------------------------------------------")
for k,v in d.items():
    print(k,"--->",v,type(d))
print("----------------------------------------------")