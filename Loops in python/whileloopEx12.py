#
# #whileloopEx12.py
# n=int(input("Enter Number for Cal Factorial:"))
# if(n<=0):
#     print("{} is a invalid input".format(n))
# else:
#     i=1
#     p=1
#     while(i<=n):
#         p=p*i
#         i=i+1
#     else:
#         print("*" * 50)
#         print("Factorial({})=({}*{})={}".format(n, p))

n=int(input("Enter a Number for Calculate Factorial:"))
if(n<0):
    print("{} is Invalid Input.".format(n))
else:
    print("*"*50)
    print("Factorial for {}".format(n))
    print("*"*50)
    i=n
    f=1
    while (i>=1):
        print("\t{}".format(i))
        f=f*i
        i=i-1
    else:
        print("*" * 50)
        print("Factorial({})={}".format(n,f))
        print("*" * 50)





