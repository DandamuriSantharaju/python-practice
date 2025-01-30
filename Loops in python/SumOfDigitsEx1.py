#Program for accepting a Number and Its Digits sum
#SumOfDigitsEx1.py
n=int(input("Enter any number:"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    ds=0
    for d in str(n):
        ds=ds+int(d)
    else:
        print("SumOfDigits({})={}".format(n,ds))