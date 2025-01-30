#Program for getting Value as Key and Key as Value from Dict
#DictComprehensionEx3.py
d={10:"PYTHON",20:"HTML",30:"CSS",40:"DJANGO",50:"MYSQL"}
d1={value:key for key,value in d.items()}
print("Original Dict")
print(d)
print("Reversed Dict")
print(d1)
print("==============================================================================")
rd={}
for k in d:
    rd[d.get(k)]=k
else:
    print("Original Dict")
    print(d)
    print("Reversed Dict")
    print(rd)







# for value,key in d.items():
#     print("{}\t\t\t{}".format(value,key))