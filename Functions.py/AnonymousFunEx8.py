
#AnonymousFunEx8.py
def rajmax(lst):
    maxv=lst[0]
    for val in lst:
        if(val>maxv):
            maxv=val
    return maxv
def rajmin(lst):
    minv=lst[0]
    for val in lst:
        if(val<minv):
            minv=val
    return minv

#Anonymous Function  Defs
findmax=lambda lst:rajmax(lst)
findmin=lambda lst:rajmin(lst)

#main Program
print("Enter list of values separated by comma:")
lst=[float(val) for val in input().split(",")]
#Calling Anonymous Funs
maxv=findmax(lst)
minv=findmin(lst)
print("max({})={}".format(lst,maxv))
print("minv({})={}".format(lst,minv))








