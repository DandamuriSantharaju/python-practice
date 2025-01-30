
#SimpleIntAapr4.py
def siplint():
    p=float(input("Enter the Principal amount:"))
    t=float(input("Enter time:"))
    r=float(input("Enter the Rate of Interest:"))
    if(p<=0) or (r<=0) or (t<=0):
        print("Invalid Input")
    else:
        si=(p*t*r)/100
        totamt=si+p
        return p,t,r,si,totamt
    #Main Program
res=siplint() # Function Call--returns either str or tuple type
if(type(res)==str):
    print(res)
else:
    print("------------------------------------------")
    print("Principal amount is {}".format(res[-5]))
    print("Time is {}".format(res[-4]))
    print("Rate of Intrest is {}".format(res[-3]))
    print("Simple Intrest is {}".format(res[-2]))
    print("Total amount is {}".format(res[-1]))
    print("-------------------------------------------")