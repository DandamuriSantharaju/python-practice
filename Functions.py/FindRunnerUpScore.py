
#FindRunnerUpScore.py
def scoreop():
    nov=int(input("Enter How many plyers socre:"))
    if(nov<=0):
        return []
    else:
        lst=[]
        for i in range(1,nov+1):
            lst.append(int(input("Enter {} Score:".format(i))))
        return lst
def Runerupscore():
    lst=scoreop()
    if(len(lst)==0):
        print("There is no score--can't find runner up score")
    else:
        score=sorted(set(lst))
        print("Runner Up Score")
        print(score)
        print("Runner-up score={}".format(score[-2]))

#main program
Runerupscore()