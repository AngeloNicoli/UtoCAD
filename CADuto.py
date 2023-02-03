from tkinter import *

canvas_width = 700
canvas_height = 450
n_seg = 0
Polygon = []

def paint( event ):
   global n_seg
   global Polygon
   print(n_seg)
   python_green = "#476042"
   print(event.x,event.y)
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = python_green )
   Polygon.append(event.x)
   Polygon.append(event.y)
   print(Polygon)
   print("n_seg" + str(n_seg))
   counter = [0,1,2,3]
   print(counter)

   
   if n_seg >= 1:
      for el in range(len(counter)):
         counter[el] += ((2 *n_seg)-2)
      print(counter)

   if n_seg >= 1:
      w.create_line(Polygon[counter[0]],Polygon[counter[1]],Polygon[counter[2]],Polygon[counter[3]])
   n_seg +=1
   #old = [event.x, event.y]

master = Tk()
master.title( "CADuto")
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height,
           bg="gray")
w.grid(row=1, column=0)
w.bind( "<Button-1>", paint )
   
e = Entry(master, width=50)
e.grid(row=2, column=0, sticky="WE", padx=5)
e.insert(0, "Comandi: ")

# Lista di Python (è piu' facile l'edit)
options =[
    "Op1",
    "Op2",
    "Op3"
]

clicked =StringVar()
clicked.set("Menu")

drop = OptionMenu(master,clicked,*options)
drop.grid(row=0, column=0, columnspan=3, sticky="W")


status = Label(master, text="CADuto ", bd = 1, relief= SUNKEN, anchor=E)
status.grid(row=3, column=0, columnspan=3, sticky="WE")
mainloop()