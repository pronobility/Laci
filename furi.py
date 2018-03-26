from tkinter import *
def circle(x, y, r, color ='black'):
 "r sugarú (x,y) középpontú lör rajzolása"
 can.create_oval(x-r, y-r, x+r, y+r, outline=color)

def figure_1():
 "celtablat rajzol"
 # el ször a meglév rajz törlése : ő ő
 can.delete(ALL)
 # a két egyenes rajzolása (függ. és vizsz.) :
 can.create_line(100, 0, 100, 200, fill ='blue')
 can.create_line(0, 100, 200, 100, fill ='blue')
 # több koncentrikus kör rajzolása :
 radius = 15
 while radius < 100:
     circle(100, 100, radius)
     radius += 15

def figure_2():
 "egyszer sített arc rajzolása" 
 # el ször minden meglév rajz törlése : ő ő
 can.delete(ALL)
 # minden kör jellemz jét listák listájába ő
 # tesszük :
 cc =[[100, 100, 80, 'red'], # fej
 [70, 70, 15, 'blue'], # szem
 [130, 70, 15, 'blue'],
 [70, 70, 5, 'black'],
 [130, 70, 5, 'black'],
 [44, 115, 20, 'red'], # arc
 [156, 115, 20, 'red'],
 [100, 95, 15, 'purple'], # orr
 [100, 145, 30, 'purple']] # száj
 # az osszes kort egy ciklus segitsegevel rajzoljuk meg :
 i =0
 while i < len(cc): # a lista bejárása
     el = cc[i] # minden elem maga is lista
     circle(el[0], el[1], el[2], el[3])
     i += 1
##### F programm : ############ ő

window = Tk()
can = Canvas(window, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(window, text ='1. ábra', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(window, text ='2. ábra', command =figure_2)
b2.pack(side =RIGHT, padx =3, pady =3)
window.mainloop()
