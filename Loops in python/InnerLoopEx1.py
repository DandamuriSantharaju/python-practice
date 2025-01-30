
#InnerLoopEx1.py------------------for loop in for loop
# for i in range(1,6):
#     print("*" * 50)
#     print("Outer loop: Value of i=", i)
#     print("*" * 50)
#     for j in range(1,4):
#         print("\t\tInner loop: Value of j=", j)
#     else:
#         print("\tOut-off inner loop")
#         print("-" * 50)
# else:
#     print("Out-off Outer loop")
#     print("*" * 50)
for i in range(1,6):
    print("*"*50)
    print("\tOuter loop: value of i=",i)
    print("*"*50)
    for j in range(1,4):
        print("\t",j)
    else:
        print("="*50)
else:
    print("*50")