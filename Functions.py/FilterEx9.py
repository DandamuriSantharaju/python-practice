
#FilterEx9.py
print("Enter List of Words separated by space")
words=[val for val in input().split()]
print("Given Words=",words)

word34=list(filter(lambda word: not(set(word.lower()).isdisjoint((set("aeiou"))))and len(word) in [3,4],words))
print("Vowel words with 3 or 4 in length")
print(word34)