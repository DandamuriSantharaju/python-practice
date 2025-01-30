#Program for accepting  Value whether it is palindrome or not
#Simple ifEx3.py
n=input("Enter a value :")
if(n==n[::-1]):
    print("\tThe value is '{}' palindrome".format(n))
if(n!=n[::-1]):
    print("\tThe value is {} not a palindrome".format(n))
print("The execution is completed")