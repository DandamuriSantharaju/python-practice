
#Perfect num with in 1000.py
def findfactors(n):
    for i in range(1, n+1):
        pr= 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                pr=pr+j
        else:
            if (pr==i):
                print("Perfect number is: {}".format(i))
# Main program
print("--------------------------------")
print("The Perfect Numbers With in 1000")
print("---------------------------------")
findfactors(1000)

