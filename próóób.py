# a "slave" widget-ek létrehozása :
window = Tk()
can = Canvas(window, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(window, text ='1. ábra', command =figure_1)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(window, text ='2. ábra', command =figure_2)
b2.pack(side =RIGHT, padx =3, pady =3)
window.mainloop()
