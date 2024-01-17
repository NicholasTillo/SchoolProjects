import tkinter as tk
import time
import math
main1 = tk.Tk()
main1.geometry("400x400")

mycanvas = tk.Canvas(main1, bg = "black", height = 400, width = 400)
mycanvas.pack()
x = 0
boxlist = []



class box:
    def __init__(self) -> None:
        #use -> so things like mypy can corretly identify error, __init__ should always return none 
        self.colour = "orange"
        self.posx = 200
        self.posy = 200
        self.width = 10
        self.height = 10
        self.canvas = mycanvas
        self.movex = 0
        self.movey = 0
        pass
    def draw(self):
        mycanvas.create_rectangle(self.posx + self.movex, self.posy + self.movey, self.posx + self.width + self.movex, 
        self.posy + self.height + self.movey, fill = self.colour)

def frame():
    smdn.movex = 10 * math.sin(x/10)
    smdn.movey = 10 * math.cos(x/10)
    blurb.movex = 100 * math.sin(x/100)
    blurb.movey = 100 * math.cos(x/100)
    mycanvas.delete('all')
    smdn.draw()
    blurb.draw()
    main1.update()
'''
def checkcollision(boxlist):
    for bbox in boxlist:
        #ANother loop, check through all the rest of them 
        for something in idk:
            if bbox.pos < 
'''
smdn = box()
blurb = box()
blurb.colour = "red"
blurb.posx = 100
blurb.posy = 100

boxlist.append(smdn)
boxlist.append(blurb)

while x < 40000:
    frame()
    #checkcollision(boxlist)
    time.sleep(0.01)
    x += 1
main1.mainloop()