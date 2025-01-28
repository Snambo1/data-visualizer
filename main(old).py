import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt,sympy as sy,numpy,matplotlib,numpy,numbers
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

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

#variables for the bar graph, doubles as jackass variables for the fuckin uh line graph yah
xNameShit='x'
yNameShit='y'

#this is a list to hold all the old graph shit, so when I make another graph the old one deletes
oldGraph=[]

graphFrame=tk.Frame(root,width=500, height=600,bg='#292826')
graphFrame.place(x=500,y=0)

canvasDraw = Canvas(graphFrame,bg="#292826",height=400,width=500)

#graph maker, parameters are used to determine which graph is made
def graphMaker(type,equation='',xShit=[],yShit=[]):
    if len(oldGraph)>0:
        for widget in oldGraph:
            widget.destroy()
        oldGraph.clear()
    #plt.rcParams['figure.facecolor'] = '#292826'
    if type=='line graph':
        xShit=[0,1,2,3,4,5,6]
        yShit=[]
        for i in xShit:
            yShit.append(myformula(x=i,formula=equation))
        # plt.rcParams['figure.facecolor'] = '#292826'
        # plt.rcParams['axes.facecolor']='#292826'
        fig = plt.figure(figsize = (10, 5))
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("your graph")

        fig = Figure(figsize = (5, 5), dpi = 100) 
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
        # plotting the graph 
        plot1.plot(yShit)   
    elif type=='bar graph':
        if xShit=="" or yShit=="":
            return ""
    
        xShit=xShit.split(",")
        yShit=yShit.split(",")
        yShit = [int(i) for i in yShit]

        courses = list(xShit)
        values = list(yShit)
    
        fig = plt.figure(figsize = (10, 5))
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("your graph")

        fig = Figure(figsize = (5, 5), dpi = 100) 
        # adding the subplot 
        plot1 = fig.add_subplot(111) 

        plot1.bar(courses, values, color ='maroon',width = 0.4,)
    elif type=='pie graph':
        if xShit=="" or yShit=="":
            return ""
    
        xShit=xShit.split(",")
        yShit=yShit.split(",")
        xShit=[int(i) for i in xShit]
        y=numpy.array(xShit)
    
        fig = plt.figure(figsize = (10, 5))
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("your graph")
        fig = Figure(figsize = (5, 5), dpi = 100) 
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
  
        plot1.pie(y, labels = yShit)
    elif type=='scatter plot':
        if xShit=="" or yShit=="":
            return ""
    
        xShit=xShit.split(",")
        yShit=yShit.split(",")
        xShit = [int(i) for i in xShit]
        yShit = [int(i) for i in yShit]

        xShit=numpy.array(xShit) 
        yShit=numpy.array(yShit)    
    
        fig = plt.figure(figsize = (10, 5))
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("your graph")

        fig = Figure(figsize = (5, 5), dpi = 100) 
        # adding the subplot 
        plot1 = fig.add_subplot(111) 
  
        plot1.scatter(xShit, yShit, color = '#88c999')

    canvas = FigureCanvasTkAgg(fig, master = graphFrame)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    oldGraph.append(canvas.get_tk_widget())
    oldGraph[0].pack() 
  

    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, graphFrame) 
    toolbar.update() 
    oldGraph.append(toolbar)

    raise_frame(graphFrame)
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

    matplotlib.pyplot.close()      

def create_circle(x, y, r):
    canvasDraw.create_oval(x-r, y-r, x+r, y+r, outline="white")

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
                 command = lambda:graphMaker('line graph',equation=lgraphInput.get("1.0", "end-1c")))
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
                 command = lambda:graphMaker('bar graph',xShit=bgraphInput1.get("1.0", "end-1c"),yShit=bgraphInput2.get("1.0", "end-1c")))
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
                 command = lambda:graphMaker('pie graph',xShit=pgraphInput2.get("1.0", "end-1c"),yShit=pgraphInput1.get("1.0", "end-1c")))
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
                 command = lambda:graphMaker('scatter plot',xShit=sgraphInput1.get("1.0", "end-1c"),yShit=sgraphInput2.get("1.0", "end-1c")))
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