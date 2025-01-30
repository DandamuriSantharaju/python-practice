
#AnonymousFunEx10.py
palindrome=lambda w: "{} is Palindrome".format(w) if w==w[::-1] else "{} is not Palindrome".format(w)

#main program
word=lambda:input("Enter Any Name:")
print(palindrome(word()))