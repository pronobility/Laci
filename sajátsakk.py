from sak import *
x1,y1,x2,y2=0,0,25,25
abl1 = Tk()
can1 = Canvas(abl1,bg='white',height=200,width=200)
can1.pack(side=TOP)
gomb1 = Button(abl1,text='Kilép',command=abl1.quit)
gomb1.pack(side=LEFT)
gomb2 = Button(abl1,text='Táblát rajzol',command=sakk)
gomb2.pack(RIGHT)
abl1.mainloop() # eseményfogadó indítása
abl1.destroy() # az ablak (destruction) zárása
