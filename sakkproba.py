from math import *
from tkinter import *
from random import *
#a négyzetek megcsinálása
def negyzet():
    global x1,y1,x2,y2,c,p, kocka
    i=0
    x1,y1,x2,y2=0,(0+2*p*c),c,(c+2*p*c)
    while i<4:
        can.create_rectangle(x1,y1,x2,y2,fill='black')
        i=i+1
        x1,x2=x1+2*c,x2+2*c
def psor():
    global x1,y1,x2,y2,c,p, kocka
    i=0
    x1,y1,x2,y2=(x1+c), (y1+c),(x2+c),(y2+c)
    while i<5:
        can.create_rectangle(x1,y1,x2,y2,fill='black')
        i=i+1
        x1,x2=x1-2*c,x2-2*c
def teljes():
    global x1,y1,x2,y2,c,p, kocka
    p=0
    can.delete(ALL)
    while p<4:
        negyzet()
        psor()
        p=p+1
def randi():
    global c,r,k
    t=randrange(9)
    k=randrange(9)
    x1,y1,x2,y2=(t*(c))-(c*0.90),(k*(c))-(c*0.90),(t*(c))-(c*0.10),(k*(c))-(c*0.10)
    can.create_oval(x1,y1,x2,y2,fill='red')
def cvalt():
    global c
    f=eval(mezo.get())
    c=f
    teljes()
def fofo(f):
    cvalt()
    abl1=Tk()
    can=Canvas(abl1,bg='ivory',height=8*(c),width=8*(c))
    can.grid(row =1, column =1, rowspan =8,columnspan=8, padx =10, pady =5)
    mezo=Entry(abl1)
    mezo.bind("<Return>",cvalt)
    mezo.grid(row=3, column=9)
    felirat=Label(abl1)
    felirat.configure(text='Pixel a négyzetek mérete')
    felirat.grid(row=4, column=9)
    Button(abl1,text='Kilépés',command=abl1.quit).grid(row=9,column=9)
    Button(abl1,text='Sakktábla megjelenítése:', command=teljes).grid(row=1,column=9)
    Button(abl1, text='random piros gomb:',command=randi).grid(row=2, column=9)
    abl1.mainloop()
    
#főprogram
abl1=Tk()
c=30
can=Canvas(abl1,bg='ivory',height=8*(c),width=8*(c))
can.grid(row =1, column =1, rowspan =8,columnspan=8, padx =10, pady =5)
mezo=Entry(abl1)
mezo.bind("<Return>",fofo)
mezo.grid(row=3, column=9)
felirat=Label(abl1)
felirat.configure(text='Pixel a négyzetek mérete')
felirat.grid(row=4, column=9)
Button(abl1,text='Kilépés',command=abl1.quit).grid(row=9,column=9)
Button(abl1,text='Sakktábla megjelenítése:', command=teljes).grid(row=1,column=9)
Button(abl1, text='random piros gomb:',command=randi).grid(row=2, column=9)
abl1.mainloop()

    
