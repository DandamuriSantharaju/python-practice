#ContinueEx1.py
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("I am else part of While loop")
    print("---------------------------------------------")
# My Reqriment is to display :  PYHON
print("By using while loop with continue stmt")
i=0
while(i<len(s)):
    if(s[i]=="T"):
        i=i+1
        continue
    print(s[i],end="")
    i=i+1
else:
    print("\n I am else part of whole loop")
print("---------------------------------------------")