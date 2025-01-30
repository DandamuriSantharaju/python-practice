
#ifelsestatementEx1.py
n=int(input("Enter a digit:"))
if n==0:
    print("\t{} is ZERO".format(n))
else:
    if n==1:
        print("\t{} is ONE".format(n))
    else:
        if n==2:
            print("\t{} is TWO".format(n))
        else:
            if n==3:
                print("\t{} is THREE".format(n))
            else:
                if n==4:
                    print("\t{} is FOUR".format(n))
                else:
                    if n==5:
                        print("\t{} is FIVE".format(n))
                    else:
                        if n==6:
                            print("\t{} is SIX".format(n))
                        else:
                            if n==7:
                                print("\t{} is seven".format(n))
                            else:
                                if n==8:
                                    print("\t{} is EIGHT".format(n))
                                else:
                                    if n==9:
                                        print("\t{} is NINE".format(n))
                                    else:
                                        if n>9:
                                            print("\t{} is +ve NUMBER".format(n))
                                        else:
                                            if n in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
                                                print("\t{} is -ve didit".format(n))
                                            else:
                                                print("\t{} is -ve number".format(n))