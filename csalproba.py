a=input('Aja meg az elért százalékot:')
n=0
a=int(a)
while n==0:
    if a>=80:
        jegy= 5
        n=n+1
    elif a>=60:
        jegy= 4
        n=n+1
    elif a>= 50:
        jegy= 3
        n=n+1
    elif a>=40:
        jegy=2
        n=n+1
    else:
        jegy= 1
        n=n+1
print ("a jegyed: ", jegy, "-es/ös/as")
