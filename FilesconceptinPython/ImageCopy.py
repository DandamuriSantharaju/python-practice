
##ImageCopy.py
try:
    with open("C:\\Users\\raju\\OneDrive\\Pictures\\Saved Pictures\\santharaju.jpg.png","rb") as rp:
        with open("raju.png","wb") as wp:
            imgdta=rp.read()
            wp.write(imgdta)
            print("Image Copied--verify")
except FileNotFoundError:
    print("Source Image Does not Exist")