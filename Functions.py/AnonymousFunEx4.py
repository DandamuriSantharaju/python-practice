
#AnonymousFunEx4.py
big=lambda a,b:a if a>b else b if b>a else "Both are equal"

#Main Program
print("Enter Two Values")
bv=big(float(input()),float(input()))
print("BIG=",bv)