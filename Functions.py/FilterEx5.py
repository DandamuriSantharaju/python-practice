
#FilterEx5.py
def isvovwel(words):
    res=False
    for ch in words:
        if ch.lower() in list("aeiou"):
            res=True
    return res
#Main Program
line=input("Enter a line of text")
words=line.split()
vwords=list(filter(isvovwel,words))
print("Vowel Words=",vwords)
