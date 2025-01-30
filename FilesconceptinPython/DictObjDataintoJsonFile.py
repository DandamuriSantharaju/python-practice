#DictObjDataintoJsonFile.py
import json
d={"Tno":100,"Tname":"Raju","Subjact":"Python","sal":4.5}
print(d,type(d))
with open("student.json","w") as fp:
    json.dump(d,fp)
    print("Dict data Saved as Record in file--verify")
print("-----------------------------------------------")
