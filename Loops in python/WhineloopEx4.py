# program for generating odd numbers where nis +ve numbers
#WhineloopEx4.py
n=int(input("Enter the +ve number:"))
if(n<=0):
    print(f"{n} is invalid input")
else:
    print("odd numbers")
    i=1
    while(i<=n):
        print(i)
        i=i+2