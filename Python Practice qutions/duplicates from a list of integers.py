# lst1=[10,20,30,40,50,60,10,20]
# lst2=[10,90,20,65,50,70]
# print(lst1)
# print(lst2)
# lst3=set(lst1)
# # lst4=set(lst2)
# # lst5=lst3&lst4
# print(list(lst3))
while (True):
   n=int(input("Enter How many values u have in a list:"))
   if(n<=0):
       print("\t{} is Invalid Input--try again".format(n))
   else:
       lst=[]
       for i in range(1,n+1):
           lst.append(int(input("Enter {} value :".format(i))))
       else:
           print("-----------------------------------------")
           print("Given List")
           print(lst)
           print("-----------------------------------------")

