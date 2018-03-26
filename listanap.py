nap = ['hétf ', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasarnap'] 
a, b = 0, 0
while a<25:
    a = a + 1
    b = a % 7
print (a, nap[b])
