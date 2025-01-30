#DictObjDataintoJsonData.py
d={"eno":200,"ename":"Raju","sal":4.6,"Dasignation":"SE"}
print(d,type(d))
for key,val in d.items():
    print("{}\t\t{}".format(key,val))
print("------------------------------------------------")
dictobject=str(d)
print(dictobject,type(dictobject))
print("------------------------------------------------")


