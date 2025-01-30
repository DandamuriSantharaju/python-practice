#Program for accepting List if Numebrs and get those numbers whose number length ranges btween 2 to 3
#FilterEx8.py
print("Enter List of number seperated by space")
numbers=[val for val in input().split()]
print("Given Numbers=",numbers)

nums23=list(filter(lambda num:num.isdigit() and len(num) in [2,3],numbers))
print(nums23)