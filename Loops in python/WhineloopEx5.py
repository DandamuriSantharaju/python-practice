# program for generating even numbers reversing order where ni +ve numbers
#whileloopEx5.py
n=int(input("Enter the +ve number:"))
if(n<=0):
    print(f"{n} is invalid input")
else:
    if n%2 != 0:
     n=n-1
    i=n
    while(i>=2):
        print(i)
        i=i-2
