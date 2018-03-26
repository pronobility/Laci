from tkinter import *
from random import randrange

def drawcube():
    global x1,y1,x2,y2, color
    can.create_rectangle(x1,y1,x2,y2,width=2,fill=color)
def drawlines():
    global x1,y1,x2,y2, color
    i=0
    while i<8:
        if i%2==0:
            color='white'
        else:
            color='black'
        drawcube()
        x1 +=25
        x2 +=25
        i+=1
def drawlinet():
    global x1,y1,x2,y2, color
    i=0
    while i<8:
        if i%2==0:
            color='black'
        else:
            color='white'
        drawcube()
        x1 +=25
        x2 +=25
        i+=1
def drawrow():
    global x1,y1,x2,y2, color
    x1,x2=0,25
    y1 +=25
def sakk():
    can.delete(ALL)
    global x1,y1,x2,y2, color
    k=0
    while k<4:
        drawlines()
        drawrow()
        drawlinet()
        drawrow()
        k+=1
