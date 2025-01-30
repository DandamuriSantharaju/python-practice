
#InnerLoopEx2.py--------------------while loop in while loop
i=1
while(i<=5):
    print("*"*50)
    print("Outer loop: Value of i=", i)
    print("*"*50)
    j=1
    while(j<=3):
        # print("*"*50)
        print("\t",j)
        j=j+1
    else:
        i=i+1
else:
    print("*"*50)