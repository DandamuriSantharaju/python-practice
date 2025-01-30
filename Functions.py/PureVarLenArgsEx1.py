
#PureVarLenArgsEx1.py
def disp(*raju):
    print(raju,type(raju))

#Main Program----Family of Similar Function Calls with Variable length args
disp(10,20,30,40,50) # Function Call-1 with 5 Args
disp(10,20,30,40) # Function Call-1 with 4 Args
disp(10,20,30) # Function Call-1 with 3 Args
disp(10,20) # Function Call-1 with 2 Args
disp(10) # Function Call-1 with 1 Args
disp() # Function Call-1 with Zero Args