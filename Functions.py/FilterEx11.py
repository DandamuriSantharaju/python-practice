
#FilterEx11.py
def is_uppercase(char):
    return char.isupper()
def get_uppercase_descending(data):
    uppercase_letters = list(filter(is_uppercase, data))
    return ''.join(sorted(uppercase_letters, reverse=True))
def is_lowercase(char):
    return char.islower()
def get_lowercase_Ascending(data):
    lowercase_latters = list(filter(is_lowercase,data))
    return ''.join((sorted(lowercase_latters, reverse=True)))
def is_odd_number(char):
    return char.isdigit() and int(char) % 2 != 0
def is_even_number(char):
    return (char.isdigit() and int(char) % 2 == 0)
# Main Program
data = input("Enter the data: ")
result = get_uppercase_descending(data)
print("Uppercase letters in descending order:", result)
result=get_lowercase_Ascending(data)
print("Lowercase letters in Ascending order:", result[::-1])
odd_numbers = sorted(filter(is_odd_number, data))
print("Odd numbers in ascending order:", ''.join(odd_numbers))
even_numbers = sorted(filter(is_even_number, data))
print("Odd numbers in Descending order:", ''.join(even_numbers)[::-1])