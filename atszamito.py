# -*- coding:Utf-8 -*-
sec=67998756482
ev=sec/31536000
nap= (ev % 365)
ora= (nap % 24)
perc= (ora % 60)
mperc= (perc % 60)
import math
a=math.floor(ev)
b=math.floor(nap)
c=math.floor(perc)
d=math.floor(ora)
e=math.floor(mperc)
print (a , b , d , c , e  )
