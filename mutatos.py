# Egérkattintás észlelése és helyének meghatározása egy ablakban :
from tkinter import *
def mutato(event):
 chain.configure(text = "Kattintás detektálva: X =" + str(event.x) +\
 ", Y =" + str(event.y))
ablak = Tk()
keret = Frame(ablak, width =200, height =150, bg="light yellow")
keret.bind("<Button-1>", mutato)
keret.pack()
chain = Label(ablak)
chain.pack()
ablak.mainloop()
