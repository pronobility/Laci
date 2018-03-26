from turtle import *
def csillag (meret, szin):
    j=0
    color(szin)
    while j<6:
        j=j+1
        forward (meret)
        right (144)
i=0
up()
goto(-300, 0)
k=10
while i<5:
    if i%2==0:
        sz='red'
    elif i==5:
        sz='green'
    else:
        sz='blue'
    down()
    csillag (k, sz)
    up()
    left(144)
    forward(20)
    i=i+1
    k=k+10
down()
sz='black'
csillag (k, sz)
up()
left(144)
forward(20)
k=k-10
while i<10:
    if i%2==0:
        sz='red'
    else:
        sz='blue'
    down()
    csillag (k, sz)
    up()
    left(144)
    forward(20)
    i=i+1
    k=k-10

