
#AreaAapr4.py
def arsqure():
    s=float(input("Enter the Side of the squre:"))
    print("-----------------------------------------")
    if(s<=0):
        return "Invalid Input"
    else:
        areasq=s*4
        return s,areasq
def arrect():
    l=float(input("Enter the Length of the Rectangle:"))
    b=float(input("Enter the bridth of the Rectangle:"))
    print("-----------------------------------------")
    if(l<=0) or (b<=0):
        return "Invalid Input"
    else:
        arrect=l*b
        return l,b,arrect
def arcircle():
    r=float(input("Enter the radius of the Circle:"))
    print("-----------------------------------------")
    if(r<=0):
        return "Invalid Input"
    else:
        arcir=3.14*(r**2)
        return r,arcir
def artriangle():
    b=float(input("Enter the bridth of the triangle:"))
    h=float(input("Enter the height of the triangle:"))
    print("-----------------------------------------")
    if(b<=0) or (h<=0):
        return "Invalid Input"
    else:
        artri=(1/2)*b*h
        return b,h,artri
#main Program
sq=arsqure()
ar=arrect()
ci=arcircle()
tr=artriangle()
if(type(sq)==str) or (ar==str) or (ci==str) or (tr==str):
    print(sq,ar,ci,tr)
else:
    print("================================================")
    print("Squre of the side {} \n\tArea of squre is ={}".format(sq[0],sq[1]))
    print("---------------------------------------------------")
    print("Length of the Rectangle {} \nbridth of the Rectangle {}\n\tArea of Rectangle is ={}".format(ar[0],ar[1],ar[2]))
    print("---------------------------------------------------")
    print("Radius of the Circle {} \n\tArea of Circle is ={}".format(ci[0],ci[1]))
    print("---------------------------------------------------")
    print("Bridth of the triangle {} \nHeight of the triangle {} \n\tArea of Triangle is ={}".format(tr[0],tr[1],tr[2]))
    print("===================================================")