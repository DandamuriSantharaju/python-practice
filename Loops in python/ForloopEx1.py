#Program for Displaying every character from str object by using for loop
#ForloopEx1.py
n=input("Enter a Line of Text:")
print("-"*50)
print("By using for Loop--Forward direction")
print("-"*50)
for ch in n:
    print(ch)
print('---------------OR-------------------------')
for ch in range(len(n)):
    print(n[ch])
print('---------------OR-------------------------')
for ch in range(-len(n),0):
    print(n[ch])
print("-"*50)
print("By using for Loop--Backward direction")
print("-"*50)
for i in n[::-1]:
    print(i)
print('---------------OR-------------------------')
for i in range(len(n)-1,-1,-1):
    print(n[i])
print('---------------OR-------------------------')
for i in range(-1, -(len(n)+1),-1):
    print(n[i])
print("-"*50)


















