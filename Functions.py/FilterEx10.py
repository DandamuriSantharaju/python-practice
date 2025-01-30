#write a python program which will implement the fallowing
# d={10:"python",20:"java",30:"Django",40:"DSA",50:"AI"} Get the name of the course whose whose course name length lies between 1to3
# ANS: DSA, AI
print("Enter List of keys separated by comma")
keys=[int(val) for val in input().split(',')]
print(keys)
print("Enter List of values separated by comma")
values=[val for val in input().split(',')]
print(values)
d=dict(zip(keys,values))
print(d)
courses = list(filter(lambda course: len(course) in [2,3],d.values()))
print("Course name 2 to 3 in length")
print(courses)















