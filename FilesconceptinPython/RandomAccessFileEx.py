
#RandomAccessFileEx.py
with open("stud1.data","r") as fp:
    print("Initial Index pointed by fp=",fp.tell())
    randata=fp.read(3)
    print("random Data=",randata)
    print("Initial Index pointed by fp=",fp.tell())
    randata=fp.read(8)
    print("random Data=", randata)
# reset the file pointer Index to 11 Index
    print("----------------------------------------")
    fp.seek(11)
    print("Index pointed by fp=", fp.tell())  # 11
    randata = fp.read(7)
    print("random Data=", randata)  # capital
    print("Index pointed by fp=", fp.tell())