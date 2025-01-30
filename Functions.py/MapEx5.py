#Program accepting List of Numerical values and find their Squares and Square Root
#MapEx5.py
print("Enter a list of numbers separated by space")
val=list(map(float,input().split()))
sqrval=list(map(lambda sqr:sqr**2,val))
sqrtval=tuple(map(lambda sqrt:sqrt**0.5,val))
print("-"*50)
print("\tvalue\t\tSquare value\t\tSquareroot value")
print("-"*50)
for gv,sqr,sqrt in zip(val,sqrval,sqrtval):
    print("\t{}\t\t{}\t\t\t{}".format(gv,sqr,round(sqrt,2)))
print("-"*50)