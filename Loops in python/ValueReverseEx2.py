#Program for Obtaining the Reverse of a Given Value--Logic-2
#ValueReverseEx2.py
val=input("Enter any value:")
print("Given value={}".format(val))
rval=""
for i in val[::-1]:
    rval=rval+i
else:
    print("Reversed value=",rval)




