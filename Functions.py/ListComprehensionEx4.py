#Program for accepting a line of Text and Find Even and Odd Length words
#ListComprehensionEx4.py
# lst=[10,20,8,-8,9,3.5,8.75,-78.3,0]
# print("Given List=",lst)
# print("-"*50)
# evlist=[val for val in lst if val%2==0]
# print("Even List=",evlist)
# odlist=[val for val in lst if val%2!=0]
# print("Odd List=",odlist)
# print("-"*50)

lst=input("Enter a line of text:")
wordes=lst.split()
print(wordes)
print("-"*50)
evelist=[word+":"+str(len(word)) for word in wordes if len(word)%2==0]
print("Even Words lisr=",evelist)
oddlist=[word+":"+ str(len(word)) for word in wordes if len(word)%2!=0]
print("ODD Words=",oddlist)