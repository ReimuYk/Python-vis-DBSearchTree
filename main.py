from tkinter import *
from PIL import Image,ImageTk

op_size = 40

def l_down(e):
    print(e.x,e.y)
    print("down")
def motion(e):
    print(e.x,e.y)
    c.coords(cursor,(e.x,e.y))
def l_up(e):
    print(e.x,e.y)
    print("up")

def movein(e):
    print("ininin")
def moveout(e):
    print("outoutout")

root = Tk()
image = Image.open("dicar.jpg")
image = image.resize((op_size,op_size))
im = ImageTk.PhotoImage(image)
c = Canvas(root,width=800,height=800,bg='white')
c.bind("<ButtonPress-1>",l_down)
c.bind("<Motion>",motion)
c.bind("<ButtonRelease-1>",l_up)
c.bind("<Enter>",movein)
c.bind("<Leave>",moveout)
c.pack()

cursor = c.create_image(0,0,image=im)

root.mainloop()
