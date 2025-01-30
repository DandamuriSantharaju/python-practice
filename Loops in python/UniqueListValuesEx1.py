#program for accepting List of Values and Obtains Unique Values
#UniqueListValuesEx1.py
n=int(input("Enter How many values u have:"))
if(n<=0):
    print("{} invalid input".format(n))
else:
    lst=[]
    for i in range (1,n+1):
        lst.append(float(input("Enter {} value:".format(i))))
    else:
        print("Given List of Elements")
        print(lst)
        # Logic for Obtaining Unique Values
        ulist = list()  # for adding Unique Values
        for val in lst:
            if val not in ulist:
                ulist.append(val)
        else:
            print("Unique Elements")
            print(ulist)






#wrute a python program which will accept list of words and from that words get only pailndrome words.


# n=int(input("Enter How many values u have:"))
# if(n<=0):
#     print("{} is invalid input".format(n))
# else:
#     lst=[]
#     for v in range(1, n+1):
#         lst.append(input("Enter {} words:".format(v)))
#     else:
#         print(lst)
#         # Logic for Obtaining Unique Values
#         plist=list()
#         for v in lst:
#             if v==v[::-1]:
#                 plist.append(v)
#             # print("nat")
#             # break
#         else:
#             print("palindrom values={}".format(plist))

