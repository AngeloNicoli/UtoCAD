from tkinter import *
import ctypes
from tkinter import ttk
import os

# Set zoom of Windows to 1 (Real Size Rendering)
ctypes.windll.shcore.SetProcessDpiAwareness(2)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Main Menu
currentResolution = [1800,900]

main = Tk()
main.title("UtoCAD v0.1")

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

main_width = int(screen_width)
main_height= int(screen_height * 0.85)

x_position = 0  # leftmost position
y_position = 0  # uppermost position

# print(type(main_height))
print(main_height)

# Set window size and position
main.geometry(f"{main_width}x{main_height}+{x_position}+{y_position}")

main.geometry('{}x{}'.format(screen_width, main_height))
main.resizable(True,True)  # Put False to prevent resize


print("Screen width:", screen_width)
print("Screen height:", screen_height)


def res1():
     main.geometry('{}x{}'.format(800,600))
     print("Resolution Changed")

def res2():
     main.geometry('{}x{}'.format(1024, 700))
     print("Resolution Changed")

def res3():
     main.geometry('{}x{}'.format(1400, 750))
     print("Resolution Changed")

def res4():
     main.geometry('{}x{}'.format(1400, 750))
     print("Resolution Changed")

mainFrame = []

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Menu bar
menubar = Menu(main)
main.config(menu=menubar)

# First Menu column
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)

# Second Menu column
editmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)

editmenu.add_command(label="01")
editmenu.add_command(label="02")

# Third Menu column
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)

helpmenu.add_command(label="Help Index")
helpmenu.add_command(label="License")

# Fourth Menu column
resmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Resolution", menu=resmenu)

resmenu.add_command(label="Resolution: 800x600",command=res1)
resmenu.add_command(label="Resolution: 1024x700",command=res2)
resmenu.add_command(label="Resolution: 1400x750",command=res3)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Frame Creation

def CreateWorkWindow():
     global main
     # Upper Frame (Buttons)
     mainFrame.append(Frame(main,bg="#3e3e42", width=currentResolution[0], height=currentResolution[1]*0.1, highlightbackground="#3e3e42",highlightthickness=1))
     # Left Frame (Function Parameters, Colors)
     frame2 = Frame(main,bg="#252526", width=currentResolution[0]*0.1, height=currentResolution[1]*0.8, highlightbackground="black",highlightthickness=1)
     # Create Second Frame
     frame3 = Frame(main,bg="#04252c", width=currentResolution[0]*0.8, height=currentResolution[1]*0.8, highlightbackground="black",highlightthickness=1)
     frame4 = Frame(main,bg="#252526", width= currentResolution[0]*0.1, height=currentResolution[1]*0.8, highlightbackground="black",highlightthickness=1)
     frame5 = Frame(main,bg="#3e3e42", width=currentResolution[0]*1, height=currentResolution[1]*0.1, highlightbackground="black",highlightthickness=1)

     frame6 = Frame(main,bg="#2d2d30", width=currentResolution[0]*1, height=currentResolution[0]*0.02, highlightbackground="black",highlightthickness=1)

     mainFrame[0].grid(row=0,column=0, columnspan=3,sticky="sewn")
     frame2.grid(row=1,column=0,rowspan=2,sticky="sewn")
     frame3.grid(row=1,column=1,sticky="sewn")
     frame4.grid(row=1,column=2,rowspan=2,sticky="sewn")
     frame5.grid(row=2,column=1,columnspan=1, sticky="ew")
     frame6.grid(row=3,column=0,columnspan=3, sticky="sewn")

def CreateCanvas():
     global main
     #a = Canvas(mainFrame[0],bg="white", width=currentResolution[0]*0.2, height=currentResolution[1]*0.2, highlightbackground="black",highlightthickness=1)
     #a.place(bordermode=INSIDE , relx =0.5-0.11, rely =0.5-0.11)

#CreateWorkWindow()
#print(mainFrame[0])
#CreateCanvas()

def Draw():
   CreateWorkWindow()
   print(mainFrame[0])
   CreateCanvas()  

# Layout all of the main containers
main.grid_rowconfigure(0, weight=1)
main.grid_rowconfigure(1, weight=50)
main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(2, weight=0)

clicked =StringVar()
clicked.set("Monday")

def clicked():
     pass

def Destroy():
     global mainFrame
     mainFrame[0].destroy()
     mainFrame = []
     pass

'''
# ------------------------------------------------------------------------------------------------------------------------------------------------------
drop = OptionMenu(frame1,clicked,"Monday","Tuesday","Wednesday","Thursday","Friday")
drop.place(bordermode=INSIDE ,height=50, width=100, relx =0.2)

Bttn_Line = Button(frame1, text="Line", fg="brown",bg ='#A6ABAF',padx=20)
Bttn_Line.place(bordermode=INSIDE ,height=80, width=100, relx =0.1)

Bttn_Polyline= Button(frame1, text="Polyline", fg="brown",bg ='#A6ABAF', padx=20)
Bttn_Polyline.grid(row=0, column=1)

Bttn_Polygon= Button(frame1, text="Polygon", fg="brown",padx=20)
Bttn_Polygon.grid(row=0, column=2)

Bttn_Polygon= Button(frame1, text="Brush", fg="brown",padx=20)
Bttn_Polygon.grid(row=0, column=3)

Bttn_Polygon= Button(frame1, text="Brush (Pixel)", fg="brown",padx=20)
Bttn_Polygon.grid(row=0, column=4)

Label_Tools= Label(frame1, text="Tool:", fg="White",bg = "#3e3e42" , padx=20)
Label_Tools.grid(row=0, column=5)

Bttn_Polygon=Button(frame1, text="Calculate Area", fg="brown",padx=20)
Bttn_Polygon.grid(row=0, column=6)

Bttn_Polygon=Button(frame1, text="Calculate Lenght", fg="brown",padx=20)
Bttn_Polygon.grid(row=0, column=7)

Bttn_Polygon=Button(frame1, text="Offset", fg="brown",padx=20)
Bttn_Polygon.grid(row=0, column=8)

# Pulsanti appartenenti al secondo frame
#blackbutton = Button(bottomframe, text="Black", fg="black")
#blackbutton.grid(row=0, column=0)

#Canv = Canvas(bottomframe, width=634, height=450, bg="gray")
#Canv.grid(row=1,column=0, columnspan=3)

#blackbutton = Button(bottomframe, text="Black", fg="black")
#blackbutton.grid(row=2, column=1,sticky="wesn")

'''

main.bind("a",lambda event:Draw())
main.bind("b",lambda event:Destroy())

# MainLoop'''
main.mainloop()