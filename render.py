from tkinter import *
import map
import generator
from perlin import PerlinNoiseFactory
import math
import time
size = 200
res = 40
space_range = size//res
frame_range = 0.1
root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
while True:
    canvas.create_rectangle(0, 0, 1000, 1000, fill="green")
    seed = generator.get_seed()
    #seed = 3101473988
    print(seed)
    a = map.country(seed)
    #pnf = PerlinNoiseFactory(3,seed, octaves=4, tile=(space_range, space_range, frame_range))
    def tohex(d):
        return hex(d)[2:]
  #  for x in range(size):
  #      for y in range(size):
      #      n = pnf(x / res, y / res, 0)
   #         c = int((n + 1)/2 * 255 + 0.5)
  #          canvas.create_rectangle(5 * x, 5 * y, 5 * x + 5, 5 * y + 5, fill="#00" + tohex(c) + "00", outline="#00" + tohex(c) + "00")
    canvas.create_text(40, 10, text = str(seed))
    for i in a.cities:
        canvas.create_oval(i.x - 7*math.log10(i.population), i.y - 7*math.log10(i.population), i.x + 7*math.log10(i.population), i.y + 7 * math.log10(i.population)   , fill="yellow", outline="yellow")
        canvas.create_text(i.x, i.y, text = str(i.population))
    for i in a.farms:
        canvas.create_oval(i.x - 10, i.y - 10, i.x + 10, i.y + 10, fill="red",outline='red')
        canvas.create_text(i.x, i.y, text = i.type)
    for i in a.roads:
        canvas.create_line(i.startx, i.starty, i.endx, i.endy)
        for j in a.roads:
            if i!=j and i.check_intersections(j)!=False:
                x = int(i.check_intersections(j)[0])
                y = int(i.check_intersections(j)[1])
                canvas.create_rectangle(x-3,y-3,x+3,y+3)
    root.update()
    time.sleep(10)
root.mainloop()