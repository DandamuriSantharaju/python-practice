#Program for Generating even numbers where ni +ve numbers
#WhineloopEx4.py
n=int(input("Enter the +ve Number:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    i=2
    while(i<=n):
        print(i)
        i=i+2