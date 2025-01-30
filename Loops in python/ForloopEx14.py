
#ForloopEx11.py
lst=[10,50,60,80.55,20]
s=0
print("-"*40)
print("List of values:")
print("-"*40)
for i in lst:
    print(i)
    s=s+i
else:
    print("-"*40)
    print("sum={}".format(s))
    print("Average={}".format(round(s / len(lst),2)))
    print("-"*50)












