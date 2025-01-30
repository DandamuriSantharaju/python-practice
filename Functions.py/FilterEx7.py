

#FilterEx7.py
line=input("Enter line of Text:")
words=line.split()
vwords=list(filter(lambda word:not (set(word.lower()).isdisjoint(set("aeiou"))),words))
print(vwords)