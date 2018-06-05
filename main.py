from tkinter import *
from PIL import Image,ImageTk

idcnt = 0
#(id,filename,location,text,item)
icon = []
#(id1,id2)
line = []

op_size = 40
iconlist=[]
iconname = ['dicar.jpg','njoin.jpg']

select=None
selectindex=-1
lineitem = []
textitem = []

def find_item(x,y):
    for item in icon:
        location = item[2]
        if abs(x-location[0])<op_size and abs(y-location[1])<op_size:
            return item
    return None
def refreshLine():
    global lineitem
    for l in lineitem:
        c.delete(l)
    lineitem = []
    for l in line:
        item1 = None
        item2 = None
        for ic in icon:
            if ic[0]==l[0]:
                item1 = ic
            if ic[0]==l[1]:
                item2 = ic
        loc1 = item1[2]
        loc2 = item2[2]
        pl = None
        ph = None
        if loc1[1]>loc2[1]:
            pl = loc2
            ph = loc1
        else:
            ph = loc2
            pl = loc1
        pl = (pl[0],pl[1]+int(op_size/2)+5)
        ph = (ph[0],ph[1]-int(op_size/2)-5)
        if pl[0]-ph[0]<-op_size:
            pl = (pl[0]+int(op_size/2)+5,pl[1])
        elif pl[0]-ph[0]>op_size:
            pl = (pl[0]-int(op_size/2)-5,pl[1])
        else:
            pl = pl
        ll = c.create_line(pl+ph)
        lineitem.append(ll)
def refreshText():
    global icon,textitem,icon
    for t in textitem:
        c.delete(t)
    textitem=[]
    for ic in icon:
        loc = ic[2]
        txt = ic[3]
        txt = txt+(40-len(txt))*' '
        loc = (loc[0]+int(op_size/2)+len(txt)*4+47,loc[1]+int(op_size/2)-5)
        t = c.create_text(loc,text=txt,font="time 15")
        textitem.append(t)
    
        
        
move_item = None
def event_l_down(e):
    global idcnt,selectindex,move_item
    print(e.x,e.y)
    item = find_item(e.x,e.y)
    if item == None:
        ic = c.create_image(e.x,e.y,image=select)
        icon.append([idcnt,iconname[selectindex],(e.x,e.y),'',ic])
        idcnt+=1
    else:
        move_item = item
        print(item)
    
    print("down")
def event_l_up(e):
    print(e.x,e.y)
    global move_item
    move_item = None
    print("up")

def event_m_down(e):
    print(e.x,e.y)
    item = find_item(e.x,e.y)
    if item == None:
        return
    loc = item[2]
    tv = StringVar()
    tv.set(item[3])
    en = Entry(root,textvariable=tv)
    en.place(x=loc[0],y=loc[1])
    def settext(e):
        item[3] = tv.get()
    en.bind("<Key>",settext)
    def packforget(e):
        en.place_forget()
        refreshText()
    en.bind("<Return>",packforget)

r_item_down = None
down_point = None
temp_line = None
def event_r_down(e):
    print(e.x,e.y)
    global r_item_down,down_point,temp_line
    r_item_down = find_item(e.x,e.y)
    down_point = (e.x,e.y)
    temp_line = c.create_line(down_point+down_point)
def event_r_up(e):
    print(e.x,e.y)
    global r_item_down,down_point,temp_line,line
    r_item_up = find_item(e.x,e.y)
    if r_item_down!=None and r_item_up!=None and r_item_down!=r_item_up:
        id1 = r_item_down[0]
        id2 = r_item_up[0]
        if (id1,id2) in line:
            line.remove((id1,id2))
        elif (id2,id1) in line:
            line.remove((id2,id1))
        else:
            line.append((id1,id2))
        refreshLine()
    r_item_down = None
    down_point = None
    c.delete(temp_line)
    temp_line = None

def event_motion(e):
    global temp_line,down_point,move_item
    c.coords(cursor,(e.x,e.y))
    if down_point!=None:
        c.coords(temp_line,down_point+(e.x,e.y))
        return
    if move_item!=None:
        it = move_item[4]
        c.coords(it,(e.x,e.y))
        move_item[2] = (e.x,e.y)
        refreshLine()
        refreshText()
        return


def event_movein(e):
    print("ininin")
def event_moveout(e):
    print("outoutout")
def event_key1(e):
    global cursor,select,selectindex
    print("key 1 press")
    c.delete(cursor)
    select = iconlist[0]
    selectindex = 0
    cursor = c.create_image(0,0,image=select)
def event_key2(e):
    global cursor,select,selectindex
    print("key 1 press")
    c.delete(cursor)
    select = iconlist[1]
    selectindex = 1
    cursor = c.create_image(0,0,image=select)
    

root = Tk()
for name in iconname:
    image = Image.open(name)
    image = image.resize((op_size,op_size))
    im = ImageTk.PhotoImage(image)
    iconlist.append(im)
select = iconlist[0]
selectindex = 0


c = Canvas(root,width=800,height=800,bg='white')
c.bind("<ButtonPress-1>",event_l_down)
c.bind("<ButtonRelease-1>",event_l_up)
c.bind("<ButtonPress-2>",event_m_down)
c.bind("<ButtonPress-3>",event_r_down)
c.bind("<ButtonRelease-3>",event_r_up)
c.bind("<Motion>",event_motion)
c.bind("<Enter>",event_movein)
c.bind("<Leave>",event_moveout)
root.bind("<Key-1>",event_key1)
root.bind("<Key-2>",event_key2)

c.pack()


cursor = c.create_image(0,0,image=select)

root.mainloop()
