
#ContinueEx8.py
s=input("Enter a line of Text:")
if(s==0):
    print("Word should not be empty-try again")
else:
    if (s.isspace()):
        print("Dont Enter the space--try again")
    else:
        # lst = []
        # for ch in s:
        #     lst.append(ch)
        # else:
        #     print(lst)
            st = []
            for val in s:
                if not (val.isalpha()):
                    st.append(val)
            else:
                # print("Given Alphabets")
                # print(''.join(st))
                tt=[]
                for ch in st:
                    if not (ch.isdigit()):
                        tt.append(ch)
                else:
                    print("Given Spacial")
                    print(''.join(tt))
                    th = []
                    for ch in st:
                        if  (ch.isdigit()):
                            th.append(ch)
                    print("Given Numbers")
                    print(''.join(th))






