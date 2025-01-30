
#FileCountInfo.py
# n1,nw,nc=0,0,0
# filename=input("Enter any File Name for counting number of lines,words and Chars:")
# with open(filename,"r") as fp:
#     lines=fp.readlines()
#     for line in lines:
#         n1=n1+1
#         nw=nw+len(line.split())
#         nc=nc+len(line)
#     else:
#         print("=" * 50)
#         print("Number of Lines=", n1)
#         print("Number of Words=", nw)
#         print("Number Chars=", nc)
#         print("=" * 50)
filename=input("Enter any File Name:")
with open(filename,"r") as fp:
    lines=fp.read()
    w=lines.split()
    for word in w:
        if(4<=len(word)<=5):
            print(word)