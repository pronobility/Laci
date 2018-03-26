from random import *
def randi():
    global c,r,k
    t=randrange(8)
    x1,y1,x2,y2=(t*c)-(c-5),(t*c)-(c-5),(t*c)+(c-5),(t*c)+(c-5)
    can.create_oval(x1,y1,x2,y2,fill='color')
                                                        
