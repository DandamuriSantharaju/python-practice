
#SumAvgFunsEx1.py
def readvalues():
    nov=int(input("Enter How Many value u want:"))
    if(nov<=0):
        return []
    else:
        lst=[]
        for i in range(1,nov+1):
            lst.append(float(input("Enter {} value:".format(i))))
        return lst
def sumavg(lst):
    if(len(lst)==0):
        print("List is empty--can't find sum and avg")
    else:
        print("----------------------------")
        print("Given List of Values")
        print("----------------------------")
        s=0
        for i in lst:
            print("\t{}".format(i))
            s=s+i
        else:
            print("-----------------------------------")
            print("SUM of List is=",s)
            print("AVG of List {}".format(s/len(lst)))
            print("-----------------------------------")

#Main Program
lst=readvalues()
sumavg(lst)