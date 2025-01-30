#Program for Deciding whether the given Number is prime or not
#BreakEx4.py
# n=int(input("Enter a Number:"))
# if(n<=1):
#     print("{} is invald input".format(n))
# else:
#     res="PRIME"
#     for i in range(2,n):
#         if(n%i==0):
#             res="NOT PRIME"
#             break
#     print("{} is {}".format(n,res))
print("===========================================================")
n=int(input("Enter a number:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    prime=True
    for i in range(2,n):
        if(n%i==0):
            prime=False
            break
    print("{} is prime".format(n) if prime else "{} not prime".format(n))