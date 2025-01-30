#ContinueEx1.py
s="PYTHON"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("I am else part of for loop")
print("----------------------------------------------")
#my requriment is to display : PYHON
print("By using for loop using continue stmt")
for ch in s:
    if(ch=="H"):
        continue
    print(ch,end="")
else:
    print("\n Iam else part of for loop")
print("---------------------------------------------")