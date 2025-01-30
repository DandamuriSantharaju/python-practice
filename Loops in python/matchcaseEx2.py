
#matchcaseEx2.py
import sys
print("*"*50)
print("\t\tArea of Different Figures")
print("*"*50)
print("""\t\tR.Rectangle
    \tS.Square
    \tC.circle
    \tT.Traingle
    \tE.exit""")
print("*"*50)
n=input("Enter ur choice:")
match n:
    case "R"|"r":
        print("Area of Rectangle")
        l,w=float(input("Enter the length of the Rectangle:")),float(input("Enter the Width of the Rectangle:"))
        print("\t\tArea of Rectangle is ({},{})={}".format(l,w,(l*w)))
    case "S"|"s":
        print("Area of Square")
        a= float(input("Enter the Side of the Square:"))
        print("\t\tArea of Rectangle is ({})={}".format(a,(a*2)))
    case "C"|"c":
        print("Area of Circle")
        r= float(input("Enter the Radius of the Circle:"))
        print("\t\tArea of Rectangle is ({})={}".format(r,3.14*(r**2)))
    case "T"|"t":
        print("Area of Trangle")
        b,h= float(input("Enter the base of tangle:")),float(input("Enter the height of trangle:"))
        print("\t\tArea of Rectangle is ({},{})={}".format(b,h,(1/2)*b*h))
    case "E"|"e":
        print("Thx for Using this Program")
        sys.exit()
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("Match case completed")
















