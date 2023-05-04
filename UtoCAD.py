from tkinter import *

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Create Main Menu
main = Tk()
main.geometry('{}x{}'.format(1400, 750))
main.resizable(False,False)
main.title("UtoCAD v0.1")

def res1():
     main.geometry('{}x{}'.format(800,600))
     print("i")

def res2():
     main.geometry('{}x{}'.format(1024, 700))
     print("i")

def res3():
     main.geometry('{}x{}'.format(1400, 750))
     print("i")

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

# Upper Frame
frame1 = Frame(main,bg="#3e3e42", width=800, height=60, highlightbackground="black",highlightthickness=1)
frame1.grid(row=0,column=0, columnspan=3 , sticky="sewn")

# Create Thir Frame
frame2 = Frame(main,bg="#252526", width=80, height=50, highlightbackground="black",highlightthickness=1)
frame2.grid(row=1,column=0,rowspan=2, sticky="sewn")

# Create Second Frame
frame3 = Canvas(main,bg="#04252c", width=640, height=50, highlightbackground="black",highlightthickness=1)
frame3.grid(row=1,column=1,sticky="sewn")

frame4 = Frame(main,bg="#252526", width= 80, height=30, highlightbackground="black",highlightthickness=1)
frame4.grid(row=1,column=2,rowspan=2,sticky="sewn")

frame5 = Frame(main,bg="#3e3e42", width=800, height=30, highlightbackground="black",highlightthickness=1)
frame5.grid(row=2,column=1,columnspan=1, sticky="ew")

frame6 = Frame(main,bg="#2d2d30", width=800, height=30, highlightbackground="black",highlightthickness=1)
frame6.grid(row=3,column=0,columnspan=3, sticky="sewn")

# layout all of the main containers
main.grid_rowconfigure(0, weight=1)
main.grid_rowconfigure(1, weight=50)
main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(2, weight=0)


# ------------------------------------------------------------------------------------------------------------------------------------------------------
#First Frame
Bttn_Line = Button(frame1, text="Line", fg="brown",bg ='#A6ABAF',padx=20)
Bttn_Line.grid(row=0, column=0,)

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



# MainLoop
main.mainloop()