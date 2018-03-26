# A Tkinter grafikus könyvtárat és a math modult alkalmazó gyakorlat
from tkinter import *
from math import *
# annak az akciónak a definíciója, amit akkor kell végrehajtani, ha a
# felhasználó az adatbeviteli mez szerkesztése után « ő Enter » -t nyom:
def kiertekel(event):
 chain.configure(text = "Eredmény = " + str(eval( mezo.get())))
# ----- F program : ----- ő
ablak = Tk()
mezo = Entry( ablak)
mezo.bind("<Return>", kiertekel)
mezo.pack()
chain = Label( ablak)
chain.pack()
ablak.mainloop()
