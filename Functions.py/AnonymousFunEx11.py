
#AnonymousFunEx11.py
vowel=lambda word: "{} is a vowel word".format(word) if any(char.lower() in "aeiou" for char in word) else "{} is not a vowel word".format(word)

#main Program
word=lambda:input("Enter a word:")
print(vowel(word()))



