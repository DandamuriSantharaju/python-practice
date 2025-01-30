#Program for Demonstrating the need fo break statement--for loop
#BreakEx2.py
s="MISSISSIPPI"
print("By using for loop")
for ch in s:
    print(ch)
else:
    print("I am else part of for loop")
    print("---------------------------------------")
#My Requirement is to display only "MISS" without using Indexing and Slicing
ctr=0
for ch in s:
    if(ch=="I"):
        ctr=ctr+1
        if(ctr==4):
          break
    print(ch,end="")
else:
    print("I am else part of for loop")
print()
print("other statement")
print("================================================================================")
i=0
while(i<len(s)):
    print(s[i])
    i=i+1
else:
    print("I am else part of whileloop")
    print("----------------------------------------")
#My Requirement is to display only "MISS" without using Indexing and Slicing
ct=0
ctr=0
while(ct<len(s)):
    if(s[ct]=="I"):
        ctr=ctr+1
        if(ctr==4):
            break
    print(s[ct],end="")
    ct=ct+1
else:
    print("I am else part of whileloop")
print()
print("other statements")
