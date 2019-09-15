import PIL
from PIL import Image


choice = int(input("Select One:\n\n\t1.Enter Width and Height.\n\t2.Enter Width (Auto Scale Height)\nEnter Option: "))
file_path = input("Enter Path: ")
img = Image.open(file_path)
if choice == 1:
    width = int(input("Enter Width : "))
    height = int(input("Enter Height : "))
elif choice == 2:
    width = int(input("Enter Width : "))
    wpercent = (width/float(img.size[0]))
    height = int((float(img.size[1])*float(wpercent)))
    
img = img.resize((width,height), PIL.Image.ANTIALIAS)
img.save('newfile.png')