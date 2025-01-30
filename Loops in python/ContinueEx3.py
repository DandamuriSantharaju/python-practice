#ContinueEx3.py
s="PYTHON"
print("by using for loop")
for ch in s:
    print(ch)
else:
    print("I am else part of for loop")
    print("---------------------------------------------")
#MY requirement is display
print("By using for loop with contune stmt")
for ch in s:
    if ch in ["T","O"]:
        continue
    print(ch,end="")
else:
    print("\nI am else part of for loop")
print("-----------------------------------------------------")

