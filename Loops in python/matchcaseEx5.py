
#matchcaseEx5.py
print("*"*50)
print("\t\tBASE CONVERTION CALCULATOR")
print("*"*50)
print("""\t\t1.D to B, D to O, D to H
        2.B to D, B to O, B to H
        3.O to D, O to B, O to H
        4.H to D, H to B, H to O""")
print("*"*50)
n=int(input("Enter ur choice :"))
print("*"*50)
match n:
    case 1:
        d=int(input("Enter the DecimalNumber :"))
        print("\tDec {} to Bin {}".format(d,(bin(d))))
        print("\tDec {} to Oct {}".format(d,(oct(d))))
        print("\tDec {} to Hex {}".format(d, (hex(d))))
    case 2:
        b=input("Enter the BinaryNumber :")
        c=int(b,2)
        print("\tBin {} to Dec {}".format(b, c))
        print("\tBin {} to oct {}".format(b, (oct(c))))
        print("\tBin {} to Hex {}".format(b, (hex(c))))
    case 3:
        o = input("Enter the OctalNumber :")
        a= int(o,8)
        print("\toct {} to Dec {}".format(o, a))
        print("\toct {} to Bin {}".format(o, (bin(a))))
        print("\toct {} to Hex {}".format(o, (hex(a))))
    case 4:
        h = input("Enter the HexadecimalNumber :")
        e= int(h,16)
        print("\tHex {} to Dec {}".format(h, e))
        print("\tHex {} to Bin {}".format(h, (bin(e))))
        print("\tHex {} to oct {}".format(h, (oct(e))))
    case _:
        print("Ur Selection of Operation is Wrong--try again")
print("Match case completed")









