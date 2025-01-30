n=int(input("Enter How many values u have:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1, n+1):
        lst.append(input("Enter {} words:".format(i)))
    else:
        print(lst)
        # Logic for Obtaining Unique Values
        plist=list()
        for v in lst:
            if v==v[::-1]:
                plist.append(v)
        if plist:
                print("Palindrome values: {}".format(plist))
        else:
            print("No palindrome values found.")
















# n=int(input("Enter How many values u have:"))
# if(n<=0):
#     print("{} is invalid input",format(n))
# else:
#     lst=[]
#     for i in range(1,n+1):
#         lst.append(input("Enetr {} value:".format(i)))
#     else:
#         print(lst)
#         vlist=list()
#         for word in lst:
#             if word.lower()  in list("aeiou"):
#                 vlist.append(word)
#                 break
#         if vlist:
#             print("not vowel words {}".format(vlist))
#         else:
#             print("vowel words")




































# n = int(input("Enter how many values you have: "))
# if n <= 0:
#     print("{} is invalid input".format(n))
# else:
#     lst = []
#     for i in range(1, n + 1):
#         lst.append(input("Enter value {}: ".format(i)))
#
#     print("Input list:", lst)
#
#     vlist = []
#     vowels = ('a', 'e', 'i', 'o', 'u')
#
#     # Check if each word starts with a vowel
#     for word in lst:
#         if word.lower() not in vowels:  # Check if the word starts with a vowel
#             vlist.append(word)
#
#     if vlist:
#         print("Words starting with vowels: {}".format(vlist))
#     else:
#         print("No words starting with vowels found.")