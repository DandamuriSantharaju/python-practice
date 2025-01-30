#program for accepting a Word and decide vowelWord are Not VowelWord
#TernaryOpEx9.py
l=input("Enter the word:")
rel= "VowelWord" if (char in "aeiou" for char in l) else "Not VowelWord"
print("\t{} is {}".format(l,rel))