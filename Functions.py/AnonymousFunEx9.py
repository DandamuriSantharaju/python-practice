
#AnonymousFunEx9.py

# Lambda function to check if a number is prime
prime = lambda a: "{} is a prime number".format(a) if a > 1 and all(a % i != 0 for i in range(2, int(a**0.5) + 1)) else "{} is not a prime number".format(a)

# Main Program
num = int(input("Enter any number: "))
print(prime(num))
