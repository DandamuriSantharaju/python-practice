
#Python Reversing a List.py
# lst1=[10,20,30,40,50,60]
# print(lst1)
# lst1.reverse()
# print(lst1)
# print("------------------------------------")
# lst2=[10,20,30,40,50,60]
# print(lst2)
# print(lst2[::-1])
# print("------------------------------------")
# lst3=[10,20,30,40,50,60]
# print(lst3)
# for x in enumerate(lst3[::-1]):
# 	print(x,end="")
# print("\n------------------------------------")
# while(True):
# 	n = int(input("Enter how many values u have in list:"))
# 	if(n<=0):
# 		print("\t{} is Invalid  Number--try again".format(n))
# 	else:
# 		lst=[]
# 		for i in range(0,n):
# 			lst.append(input("Enter {} value:".format(i)))
# 		else:
# 			print(lst)
# 			# lst.reverse()
# 			print("Reversing a List ={}".format(lst))
# 			break
# print("\n------------------------------------")
# while(True):
# 	n = int(input("Enter how many values u have in list:"))
# 	if(n<=0):
# 		print("\t{} is Invalid  Number--try again".format(n))
# 	else:
# 		lst=[]
# 		for i in range(0,n):
# 			lst.append(input("Enter {} value:".format(i)))
# 		else:
# 			print(lst)
# 			print("Reversing a List ={}".format(lst[::-1]))
# 			break
# print("\n------------------------------------")
# while(True):
# 	n = int(input("Enter how many values u have in list:"))
# 	if(n<=0):
# 		print("\t{} is Invalid  Number--try again".format(n))
# 	else:
# 		lst=[]
# 		for i in range(0,n):
# 			lst.append(input("Enter {} value:".format(i)))
# 		else:
# 			lst1=[]
# 			for x in enumerate(lst[::-1]):
# 				lst1.append(x)
# 				# print(x,end="")
# 			else:
# 				print(f"Reversing a List ={lst1}",end="")
# 				break
print("\n------------------------------------")
# while(True):
# 	n = input("Enter how many values u have in list:")
# 	if(len(n)=="0"):
# 		print("\t{} is Invalid  Number--try again".format(n))
# 	else:
# 		lst=[]
# 		i=0
# 		while (i<int(n)):
# 			val=input("Enter {} value:".format(i))
# 			lst.append(val)
# 			i=i+1
# 		else:
# 			print(lst)
# 			print()
# 			print("Reversing a List ={}".format(lst[::-1]))
# 			break
print("---------------------------------------------------------")
while(True):
	n = input("Enter how many values u have in list:")
	if(len(n)=="0"):
		print("\t{} is Invalid  Number--try again".format(n))
	else:
		lst=[]
		i=0
		while (i<int(n)):
			val=input("Enter {} value:".format(i))
			lst.append(val)
			i=i+1
		else:
			print(lst)
			lst.reverse()
			print("Reversing a List ={}".format(lst))
			break
print("-----------------------------------------------------------")






