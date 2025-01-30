
#InnerLoopEx4.py--------------------while loop in for loop
for i in range(1,6):
    print("*"*50)
    print("Outer loop: Value of i=", i)
    print("*"*50)
    j=1
    while(j<=3):
         print("\t\tInner loop: Value of j=", j)
         j=j+1
    else:
        print("="*50)
else:
    print("*"*50)

