
#NumberPalindromeEx1.py
n=int(input("Enter any numarical value:"))
print("Give number={}".format(n))
rn=0
tn=n
while(n>0):
    r=n%10
    rn=rn*10+r
    n=n//10
else:
    if (tn==rn):
        print("{} is Palindrome".format(tn))
    else:
        print("{} is not a palindrome".format(tn))
