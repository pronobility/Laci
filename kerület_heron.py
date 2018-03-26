from math import *
a=input()
b=input()
c=input()
a=float(a)
b=float(b)
c=float(c)
d=(a+b+c)/2
print (d)
g=(d*(d-a)*(d-c)*(d-b))
print (g)
k=sqrt(g)
print("a kerület:", (d*2))
print("a terület:",k)
