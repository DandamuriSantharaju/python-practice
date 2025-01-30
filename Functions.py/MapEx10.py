
#MapEx10.py
lst1=list(map(float,input("Enter First list elements seperated by space").split()))
lst2=list(map(float,input("Enter Second list elements seperated by space").split()))
if(len(lst1)>len(lst2)):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0)
elif(len(lst2)>len(lst1)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0)
sumlist=list(map(lambda a,b:a+b,lst1,lst2))
print("-"*50)
print("\tList1\t\t\tList2\t\t\tSumList")
print("-"*50)
for val1,val2,val3 in zip(lst1,lst2,sumlist):
    print("\t{}\t\t{}\t\t{}".format(val1,val2,val3))
print("-"*50)

