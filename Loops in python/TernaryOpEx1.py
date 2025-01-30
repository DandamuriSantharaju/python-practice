#Program for Reading the Value from KBD and Decide whether It is Palindrome or Not
#TernaryOpEx1.py
p=input("Enter a vlue:")
rel="Palindrome" if p==p[::-1] else " not aPalindrome"
print("\t{} is {}".format(p,rel))











