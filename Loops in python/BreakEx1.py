#Program for Demonstrating the need fo break statement--for loop
#BreakEx1.py
s="santharoju"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("I am else part of for loop")
    print("----------------------------------------")
#My Requirement is to display only "PYTH" without using Indexing and Slicing
print("By using with break statement")
for ch in s:
    if(ch=="o"):
        break
    print(ch,end="")
else:
    print("\t\tI am from else part of for loop")
print()
print("Other statements in Program")







