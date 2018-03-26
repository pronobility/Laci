# Tkinter grafikus könyvtárat alkalmazó gyakorlat
from tkinter import *
from random import randrange
# --- az eseménykezel függvények definíciója : --- ő
def drawline():
 "Vonal rajzolása a can1 canvasra (vászonra)"
 global x1, y1, x2, y2, color
 can1.create_rectangle(x1,y1,x2,y2, width=2,fill=color)
 # a koordináták módosítása a következ egyenes számára : ő
 y2, y1, x1, x2 = (x2*-1), x1,y1, y2
def changecolor():
 "a rajz színének véletlenszer megváltoztatása" 
 global color
 pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
 c = randrange(8) # => véletlenszám generálása 0 és 7 között
 color = pal[c]
#------ F program ------- ő
# a következ változókat globális változókként használjuk : ő
x1, y1, x2, y2 = 0, 25, 25, 50 # az egyenes koordinátái
color = 'dark green' # az egyenes színe
# A f -widget létrehozása ("master") : ő
abl1 = Tk()
# a "slave" widget-ek létrehozása :
can1 = Canvas(abl1,bg='dark grey',height=500,width=650)
can1.pack(side=LEFT)
gomb1 = Button(abl1,text='Kilép',command=abl1.quit)
gomb1.pack(side=BOTTOM)
gomb2 = Button(abl1,text='Vonalat rajzol',command=drawline)
gomb2.pack()
gomb3 = Button(abl1,text='Más szín',command=changecolor)
gomb3.pack()
abl1.mainloop() # eseményfogadó indítása
abl1.destroy() # az ablak (destruction) zárása
