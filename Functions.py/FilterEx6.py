#Program for accepting line of Text and get those words which contains at least one one Vowel
#FilterEx6.py
def isvowel(word):
    res=not(set(word.lower()).isdisjoint((set("aeiou"))))
    return res
#Main Program
line=input("Enter line of text:")
words=line.split()
vwords=list(filter(isvowel,words))
print("Vowel Words=",vwords)


