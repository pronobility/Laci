from turtle import *
def har(szin):
    color(szin)
    forward(150)
    left (120)
    forward(150)
    left(120)
    forward(150)
a=input('írjon be egy színt')
c=input("írjon be egy szöget:")
c=int(c)
b=1
reset()
while b<5:
    har(a)
    left(c)
    b=b+1

