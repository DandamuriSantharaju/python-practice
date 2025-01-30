#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
		#Sample List : ['abc', 'xyz', 'aba', '1221']
		#Expected Result : 2
#first&last char are same from a given list.py
from itertools import count

n=int(input("Enter How many values U have:"))
if n<=0:
    print("{} is invalid input".format(n))
else:
    lst=[]
    for i in range(1,n+1):
        val=input("Enter {} value:".format(i))
        lst.append(val)
    count =0
    for val in lst:
        if len(val) >=2 and val[0] == val[-1]:
            count+=1
    print("Given List=",lst)
    print("Expected Result:", count)








