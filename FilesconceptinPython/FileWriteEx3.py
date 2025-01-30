#Program for writing the Iterable Object Data to the file
#FileWriteEx3.py
x=[10,"SANTHARAJU",45623.12]
with open("stud1.data","a+") as fp:
    fp.writelines(str(x)+"\n")
    print("Iterable Object Data written to the File")
