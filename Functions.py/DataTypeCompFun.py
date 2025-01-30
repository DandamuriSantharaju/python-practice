
#DataTypeCompFun.py
def dispval(x):
    if(type(x)==int):
        print("Value:{} Type:{}".format(x,type(x)))
    elif(type(x)==float):
        print("value:{} Type:{}".format(x,type(x)))
    elif(type(x)==bool):
        print("value:{} Type:{}".format(x,type(x)))
    elif(type(x)==complex):
        print("value:{} Type:{}".format(x,type(x)))
    elif(type(x)==str):
        print("value:{} Type:{}".format(x,type(x)))
    elif(type(x)==bytes):
        print("Value:{} Type:{}".format(x,type(x)))
    elif(type(x)==bytearray):
        print("value:{} Type:{}".format(x,type(x)))
    elif (type(x) == range):
        print("value:{} Type:{}".format(x, type(x)))
        for i in range(10,21,2):
            print("\t\t{}".format(i))
    elif (type(x) == list):
        print("value:{} Type:{}".format(x, type(x)))
    elif (type(x) == tuple):
        print("value:{} Type:{}".format(x, type(x)))
    elif (type(x) == set):
        print("value:{} Type:{}".format(x, type(x)))
    elif (type(x) == frozenset):
        print("value:{} Type:{}".format(x, type(x)))
    elif (type(x) == dict):
        print("value:{} Type:{}".format(x, type(x)))
        for v,l in x.items():
            print("\t\t{}---->{}".format(v,l))
    else:
        print("value:{} Type:{}".format(x, type(x)))


#Main Program
print("Fundamental Category DataType")
print("------------------------------")
dispval(10) # Function with int type
dispval(25.32) #Function With float type
dispval(True) #Function with bool type
dispval(2+7j) #Function with Complex type
print("-------------------------------")
print("Sequence Category DataType")
print("-------------------------------")
dispval("Santharaju") #Function with string type
dispval(bytes([10,50,25,62,1])) #Function with Complex type
dispval(bytearray([12,25,60,45,0,78])) #Function with Complex type
dispval(range(10,21,2)) #Function with Complex type
print("---------------------------------------")
print("List Category DataType")
print("---------------------------------------")
dispval([10,15,-89,0,366]) #Function with list type
dispval(list("Santharaju"))  #Function with list type
dispval(tuple("Tuple")) #Function with tuple type
dispval((10,56,-7,59)) #Function with tuple type
print("---------------------------------------")
print("set Category DataType")
print("---------------------------------------")
dispval({10,20,10,15,-8,9,45}) #Function with set type
dispval(set("raju")) #Function with set type
dispval(frozenset((10,25,0,-78,69,258))) #Function with frozenset type
dispval(frozenset("Santharaju")) #Function with frozenset type
print("---------------------------------------")
print("dict Category DataType")
print("---------------------------------------")
dispval({10:56,20:1.5,30:2.6,40:8.1}) #Function with dict type
dispval(dict([(10,'sa'),(20,'nt'),(30,'ha'),(40,'ra'),(50,'ju')])) #Function with dict type
dispval(dict(zip(["Python","c","html","css","java"],[1,2,3,45]))) #Function with dict type
print("---------------------------------------")
print("NoneType Category DataType")
print("---------------------------------------")
dispval(None)
print("=======================================")


