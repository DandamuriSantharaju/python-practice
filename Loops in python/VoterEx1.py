#Program for Deciding weather the citizen is Eligible Vote Or Not
#VoterEx1.py
age=int(input("Enter ur age:"))
if(age<18):
    print("{} Years Citizen is not elgible to vote".format(age))
else:
    print("{} Years Citizen is elgible to vote".format(age))