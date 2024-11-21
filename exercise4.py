quad_zahl=[]   #leere liste vordefinieren

for k in range (1,11):
    if k%2==0:
        quad_zahl.append(k)
    else:
        quad_zahl.append(k**2)
        
        
print(quad_zahl)

#Alternative
quad_zahl_neu=[zahl  if zahl%2==0 else zahl**2 for zahl in range (1,11)]
print(quad_zahl_neu)