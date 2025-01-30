
#MapEx12.py
# def upper(word):
#    return word.upper()
# lst=list(map(str,filter(str.isalpha,input("Enter First list Words seperated by space:").split())))
# letter=list(map(upper,lst))
# print(letter)

lst=list(map(str,input("Enter First list Words seperated by space:").split()))
upper=list(map(lambda woard:woard.upper(),lst))
print(upper)