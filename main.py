import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import sympy as sy,math

#binary tree template
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
      self.x=None
      self.y=30

#formula assesser bitches
def myformula(formula, **kwargs):
    expr = sy.sympify(formula)
    return expr.evalf(subs=kwargs)

root = Tk()

#window setup shit
root.title("data visualizer")
root.geometry('1000x600')
ico = Image.open('penisforeskinicon.JPG')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.configure(bg='#292826')

#function to change screens
def raise_frame(frame):
    frame.tkraise()

graphFrame=tk.Frame(root,width=500, height=600,bg='#292826')
graphFrame.place(x=500,y=10)

canvasDraw = Canvas(graphFrame,bg="#292826",height=400,width=500)

def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num
  
#graph maker, parameters are used to determine which graph is made
def lineGraph(equation):
    xShit=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
    yShit=[]
    for i in xShit:
        yShit.append(myformula(x=i,formula=equation))
    raise_frame(graphFrame)
    canvasDraw.place(x=0,y=0)
    canvasDraw.delete("all")
    canvasDraw.create_line(0, 200, 500, 200,fill="white")
    canvasDraw.create_line(250, 0, 250, 400,fill="white")
    maxxer=max(yShit)
    benchmark=maxxer/5
    for i in range(len(xShit)):
        if int(maxxer-benchmark*i)!=0:
            canvasDraw.create_text(240,400/(len(xShit)-1)*i,fill="white",font="Times 8 italic bold",
                        text=formatNumber(maxxer-benchmark*i))
        canvasDraw.create_line(245, 400/(len(xShit)-1)*i, 255, 400/(len(xShit)-1)*i,fill="white")
    for i in range(len(xShit)):
        if int(maxxer-benchmark*i)!=0:
            canvasDraw.create_text(500/(len(xShit)-1)*i,195,fill="white",font="Times 8 italic bold",
                        text=xShit[i])
        canvasDraw.create_line(500/(len(xShit)-1)*i, 195, 500/(len(xShit)-1)*i, 205,fill="white")

    factor= 400/(len(xShit)-1)/benchmark
    for i in range(1,len(xShit)):
        canvasDraw.create_line(500/(len(xShit)-1)*(i-1), 200-(factor*yShit[i-1]), 
                               500/(len(xShit)-1)*i, 200-(factor*yShit[i]),fill="white")
def barGraph(xShit,yShit):
    if xShit=="" or yShit=="":
            return ""
    xShit=xShit.split(",")
    yShit=yShit.split(",")
    yShit = [int(i) for i in yShit]
    raise_frame(graphFrame)
    canvasDraw.place(x=0,y=0)
    canvasDraw.delete("all")
    canvasDraw.create_line(20, 0, 20, 380,fill="white")
    canvasDraw.create_line(20, 380, 480, 380,fill="white")
    maxxer=max(yShit)
    benchmark=maxxer/len(xShit)
    for i in range(len(xShit)):
        canvasDraw.create_text(10,380/len(xShit)*i,fill="white",font="Times 8 italic bold",
                        text=formatNumber(maxxer-benchmark*i))
    for i in range(len(xShit)):
        canvasDraw.create_text(20+480/len(xShit)*i,390,fill="white",font="Times 8 italic bold",
                        text=xShit[i])
        
    factor=400/len(xShit)/benchmark
    for i in range(len(xShit)):
        canvasDraw.create_rectangle(20+480/len(xShit)*i, 380-(factor*yShit[i]), 
                                    20+480/len(xShit)*i+480/len(xShit)/2, 380, fill='white')

#drawing a circle arc
def circular_arc(canvas, x, y, r, t0, t1, width):
    return canvas.create_arc(x-r, y-r, x+r, y+r, start=t0, extent=t1-t0,
                             style='arc', width=width,outline='white')
def create_circle(x, y, r):
    canvasDraw.create_oval(x-r, y-r, x+r, y+r, outline="white")

def pieGraph(xShit,yShit):
    if xShit=="" or yShit=="":
        return ""
    xShit=xShit.split(",")
    yShit=yShit.split(",")
    yShit = [int(i) for i in yShit]
    total=sum(yShit)
    for i in range(len(yShit)):
        yShit[i]=yShit[i]/total
    raise_frame(graphFrame)
    canvasDraw.place(x=0,y=0)
    canvasDraw.delete("all")
    prev=0
    for i in range(len(yShit)):
        circular_arc(canvasDraw,250,200,100,prev,prev+yShit[i]*360,1)
        canvasDraw.create_line(250,200,
                               math.cos(math.radians(prev+yShit[i]))*100+250,math.sin(math.radians(prev+yShit[i]))*100+200,fill='white')
        prev+=yShit[i]*360

def scatterPlot(xShit,yShit):
    xShit=xShit.split(",")
    yShit=yShit.split(",")
    xShit = [int(i) for i in xShit]
    yShit = [int(i) for i in yShit]
    raise_frame(graphFrame)
    canvasDraw.place(x=0,y=0)
    canvasDraw.delete("all")
    canvasDraw.create_line(20, 0, 20, 380,fill="white")
    canvasDraw.create_line(20, 380, 480, 380,fill="white")
    yMaxxer=max(yShit)
    yBenchmark=int(yMaxxer/len(xShit))
    xMaxxer=max(xShit)
    xBenchmark=int(xMaxxer/len(xShit))
    for i in range(len(xShit)):
        canvasDraw.create_text(10,380/len(xShit)*i,fill="white",font="Times 8 italic bold",
                        text=formatNumber(yMaxxer-yBenchmark*i))
    for i in range(len(xShit)):
        canvasDraw.create_text(20+480/len(xShit)*i,390,fill="white",font="Times 8 italic bold",
                        text=formatNumber(xMaxxer-xBenchmark*(len(xShit)-i-1)))
    yFactor=400/len(xShit)/yBenchmark
    xFactor=500/len(xShit)/xBenchmark
    for i in range(len(xShit)):
        create_circle(20+(xFactor*xShit[i]), 380-(yFactor*yShit[i]), 3)

def distance(node):
    d=[0,0]
    if node.left != None:
        d[0]=distance(node.left)
    if node.right != None:
        d[1]=distance(node.right)
    node.x=d[0]+d[1]
    if node.x==0:
        return 20
    return node.x
def recur(node,frame,x,y,offset):
    canvasDraw.create_text(x,y,fill="white",font="Times 20 italic bold",
                        text=node.data)
    create_circle(x,y,15)
    if node.left !=None:
        canvasDraw.create_line(x, y, x-node.x, y+30,fill="white")
        recur(node.left,frame,x-node.x,y+30,offset-1)
    if node.right !=None:
        canvasDraw.create_line(x, y, x+node.x, y+30,fill="white")
        recur(node.right,frame,x+node.x,y+30,offset-1)
#binary tree constructor, this one makes the actual binary tree while the other one visualizes  it
def binaryTree(data):
    data=data.split(',')
    last=data[0]
    data=data[1:]
    data=[data[n:n+2] for n in range(0, len(data), 2)]
    node=Node(last)
    buffer=[node]

    for i in data:
        if i[0] !='null':
            buffer[0].left=Node(i[0])
        if len(i)>1 and i[1] !='null':
            buffer[0].right=Node(i[1])
        if buffer[0].left!= None:
            buffer.append(buffer[0].left)
        if buffer[0].right!=None:
            buffer.append(buffer[0].right)
        buffer = buffer[1:]
        
    return node
    #for i in range(len(data)):


#binary tree maker
def makeBinaryTree(data,frame):
    btree=binaryTree(data)
    data=data.split(',')
    buf=0
    for i in data:
        if i.isnumeric():
            buf+=1
    # data=data[1:]
    # data=[data[n:n+2] for n in range(0, len(data), 2)]
    raise_frame(graphFrame)
    canvasDraw.place(x=0,y=0)
    canvasDraw.delete("all")
    distance(btree)
    recur(btree,frame,260,20,buf)

#making frames
f1 = tk.Frame(root,width=1000, height=600,bg='#292826')
f2 = tk.Frame(root,width=1000, height=600,bg='#292826')
f3 = tk.Frame(root,width=1000, height=600,bg='#292826')
f4 = tk.Frame(root,width=1000, height=600,bg='#292826')
f5 = tk.Frame(root,width=1000, height=600,bg='#292826')
f6 = tk.Frame(root,width=1000, height=600,bg='#292826')


for frame in (f1, f2, f3, f4,f5,f6):
    frame.place(x=0, y=0,width=1000,height=600)

#menu screen
Button(f1, text='line graph', command=lambda:raise_frame(f2)).place(x=10,y=10)
barButton=Button(f1, text='bar graph', command=lambda:raise_frame(f3))
barButton.place(x=0,y=0)
barButton.update()
barButton.place(x=(1000 - barButton.winfo_width()) // 2,y=10)
pieButton=Button(f1, text='pie graph', command=lambda:raise_frame(f4))
pieButton.place(x=0,y=0)
pieButton.update()
pieButton.place(x=1000 - pieButton.winfo_width()-10,y=10)
Button(f1, text='scatter plot', command=lambda:raise_frame(f5)).place(x=10,y=60)
btreeButton=Button(f1, text='binary tree', command=lambda:raise_frame(f6))
btreeButton.place(x=0,y=0)
btreeButton.update()
btreeButton.place(x=(1000 - barButton.winfo_width()) // 2,y=60)
#line graph screen
Button(f2, text='back', command=lambda:raise_frame(f1)).place(x=10,y=10)
lgraphInput = Text(f2, height = 5,
                width = 25,
                bg = "light yellow")
lgraphInput.place(x=10,y=200)
Display = Button(f2, 
                 text ="make",
                 command = lambda:lineGraph(lgraphInput.get("1.0", "end-1c")))
Display.place(x=220,y=230)

#bar graph screen 
Button(f3, text='back', command=lambda:raise_frame(f1)).place(x=10,y=10)
bgraphInput1 = Text(f3, height = 5,
                width = 25,
                bg = "light yellow")
bgraphInput1.place(x=10,y=200)
bgraphInput2 = Text(f3, height = 5,
                width = 25,
                bg = "light yellow")
bgraphInput2.place(x=10,y=300)
Display2= Button(f3, 
                 text ="make",
                 command = lambda:barGraph(bgraphInput1.get("1.0", "end-1c"),bgraphInput2.get("1.0", "end-1c")))
Display2.place(x=220,y=280)

#pie graph screen
Button(f4, text='back', command=lambda:raise_frame(f1)).place(x=10,y=10)
pgraphInput1 = Text(f4, height = 5,
                width = 25,
                bg = "light yellow")
pgraphInput1.place(x=10,y=200)
pgraphInput2 = Text(f4, height = 5,
                width = 25,
                bg = "light yellow")
pgraphInput2.place(x=10,y=300)
Display3= Button(f4, 
                 text ="make",
                 command = lambda:pieGraph(pgraphInput1.get("1.0", "end-1c"),pgraphInput2.get("1.0", "end-1c")))
Display3.place(x=220,y=280)

#scatter plot screen
Button(f5, text='back', command=lambda:raise_frame(f1)).place(x=10,y=10)
sgraphInput1 = Text(f5, height = 5,
                width = 25,
                bg = "light yellow")
sgraphInput1.place(x=10,y=200)
sgraphInput2 = Text(f5, height = 5,
                width = 25,
                bg = "light yellow")
sgraphInput2.place(x=10,y=300)
Display4= Button(f5, 
                 text ="make",
                 command = lambda:scatterPlot(sgraphInput1.get("1.0", "end-1c"),sgraphInput2.get("1.0", "end-1c")))
Display4.place(x=220,y=280)

#binary tree screen
Button(f6, text='back', command=lambda:raise_frame(f1)).place(x=10,y=10)
btreeInput = Text(f6, height = 5,
                width = 25,
                bg = "light yellow")
btreeInput.place(x=10,y=200)
Display5 = Button(f6, 
                 text ="make",
                 command = lambda:makeBinaryTree(btreeInput.get("1.0", "end-1c"),f6))
Display5.place(x=220,y=230)
raise_frame(f1)

root.mainloop()