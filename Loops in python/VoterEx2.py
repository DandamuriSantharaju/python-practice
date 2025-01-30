#Program for Deciding weather the citizen is Eligible Vote Or Not
#VoterEx2.py
while(True):
    age=int(input("Enter ur age:"))
    if(age<18):
        print("{} Years is citizen  not eligible to vote".format(age))
    else:
        print("{} Years is citizen eligible to vote".format(age))
        break