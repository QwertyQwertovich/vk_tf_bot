from tkinter import *
import map
import generator
import time
root = Tk()
width = 1000
height = 1000
canvas = Canvas(root, width=width, height=height)
canvas.pack()
canvas.create_rectangle(0, 0, 1000, 1000, fill="green")
a = map.country(generator.get_seed())
for i in a.cities:
    canvas.create_rectangle(i.x-10, i.y-10, i.x+10, i.y+10, fill="black")
for i in a.farms:
    canvas.create_rectangle(i.x-5, i.y-5, i.x+5, i.y+5, fill="red")
time.sleep(0.1)
root.update()
root.mainloop()