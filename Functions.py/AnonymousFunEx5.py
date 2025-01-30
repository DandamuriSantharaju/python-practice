
#AnonymousFunEx5.py
small=lambda a,b:a if a<b else b if b<a else "Both are equal"


#main Program
print("Enter two values")
sv=small(float(input()),float(input()))
print("SMALL=",sv)