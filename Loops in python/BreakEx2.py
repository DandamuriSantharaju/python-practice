#Program for Demonstrating the need fo break statement--while loop
#BreakEx2.py
s="PYTHON"
print("By using while loop")
i=0
while(i<(len(s))):
    print(s[i])
    i=i+1
else:
    print("I am else part of while loop")
    print("---------------------------------------")
# My Requirement is to display only "PYTH" without using Indexing and Slicing
i=0
while(i<len(s)):
    if(s[i]=="O"):
        break
    print(s[i], end="")
    i = i + 1


else:
    print("I am else part of while loop")
print()
print("other statement")
