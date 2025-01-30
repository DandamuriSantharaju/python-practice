#RomanNumToNormal.py
roman_dict = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}

rn = input("Enter a Roman numeral you want to convert to a normal number: ")
if len(rn) == 0:
    print("Invalid input: {}".format(rn))
else:
    if rn.islower():
        print("{} is invalid input".format(rn))
    else:
        nv = 0
        for i in range(len(rn)):
            cv = roman_dict.get(rn[i], 0)

            if i + 1 < len(rn):
                if (rn[i] == "I" and rn[i + 1] in "VX") or (rn[i] == "X" and rn[i + 1] in "LC") or (
                        rn[i] == "C" and rn[i + 1] in "DM"):
                    nv = nv - cv
                else:
                    nv = nv + cv
            else:
                nv = nv + cv

        print("{} has the value: {}".format(rn.upper(), nv))