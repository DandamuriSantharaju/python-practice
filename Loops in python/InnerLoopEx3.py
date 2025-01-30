
#InnerLoopEx3.py----------------------for loop in while loop
i=5
while(i>=1):
    print("*"*50)
    print("Outer loop: Value of i=", i)
    print("*"*50)
    for j in range(1,4):
        print("\t",j)
    else:
        i=i-1
else:
    print("*"*50)