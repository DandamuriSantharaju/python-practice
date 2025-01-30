
#whileloopEx10.py
n=int(input("Enter the +ve number:"))
if(n<0):
    print("{} is invalid input".format(n))
else:
    i=1
    p=1
    while(i<=n):
        print(i)
        p=p*i
        i=i+1
    else:
        print("*"*50)
        print("\t{}".format(p))


# n=int(input("Enter Number for Cal Factorial:"))
# if(n<0):
#     print("{} is Invalid Input:".format(n))
# else:
#     p=1
#     i=1
#     while(i<=n):
#         p = p * i
#         i=i+1
#     else:
#         print("-"*50)
#         print("Factorial({})={}".format(n,p))
#         print("-" * 50)

