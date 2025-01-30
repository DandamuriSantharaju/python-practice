
#BsaeconvertionFunctions.py
def menu():
    print("*"*50)
    print("BASE CONVERTION OPERATIONS")
    print("*"*50)
    print("\t\t1.D to B, D to O, D to H")
    print("\t\t2.B to D, B to O, B to H")
    print("\t\t3.O to D, O to B, O to H")
    print("\t\t4.H to D, H to B, H to O")
    print("\t\t5.EXIT")
    print("*"*50)
def decop():
    d=int(input("Enter a Dairymaid Number:"))
    print("Dec {} to Bin {}".format(d,bin(d)))
    print("Dec {} to Oct {}".format(d, oct(d)))
    print("Dec {} to Hex {}".format(d, hex(d)))
def binop():
    b=input("Enter a Binary Number:")
    c=int(b,2)
    print("Bin {} to dec {}".format(b, c))
    print("Bin {} to Oct {}".format(b, oct(c)))
    print("Bin {} to Hex {}".format(b, hex(c)))
def octop():
    o=input("Enter a Octal Number:")
    c=int(o,8)
    print("OCT {} to DEC {}".format(o, c))
    print("OCT {} to BIN {}".format(o, bin(c)))
    print("OCT {} to HEX {}".format(o, hex(c)))
def hexop():
    h=input("Enter a HexaDecimal Number:")
    c=int(h,16)
    print("HEX {} to DEC {}".format(h, c))
    print("HEX {} to BIN {}".format(h, bin(c)))
    print("HEX {} to OCT {}".format(h, oct(c)))

#main Program
while(True):
    menu()
    ch=int(input("Enter ur Choice:"))
    match(ch):
        case 1:
            decop()
        case 2:
            binop()
        case 3:
            octop()
        case 4:
            hexop()
        case 5:
            print("Thanks for using Program")
            break
        case _:
            print("Ur Selecton operation is Wrong --Try again")

