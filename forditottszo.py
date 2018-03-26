volt="radar"
n=2
k=len(volt)
uj=volt[k-1]
while n<=k:
    uj=uj+volt[k-n]
    n=n+1
print (uj)
if uj==volt:
    print ("palindrom")
else:
    print ("nem palindrom")
