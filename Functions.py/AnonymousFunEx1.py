#Prpogram for Cal addiution of Two Numbers by using Anonymous Function
#AnonymousFunEx1.py
sumop=lambda a,b:a+b

#Main Program
print("Type of sumop=",type(sumop))
print("--------------------------------")
print("Enter Two Values")
res=sumop(float(input()),float(input()))
print("Sum By using Anomynous Function=",res)
