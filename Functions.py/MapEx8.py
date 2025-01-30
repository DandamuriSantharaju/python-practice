
#MapEx8.py
def sum(x,y):
    return x+y
print("Enter First list elements seperated by space")
lst1=list(map(float,input().split()))
print("Enter First list elements seperated by space")
lst2=list(map(float,input().split()))
lst3=list(map(sum,lst1,lst2))
print("-"*50)
print("\tList1\t\tList2\t\tSumList")
print("-"*50)
for val1,val2,val3 in zip(lst1,lst2,lst3):
    print("\t{}\t\t\t{}\t\t\t{}".format(val1,val2,val3))
print("-"*50)