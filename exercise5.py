import matplotlib.pyplot as plt

#Parameter für die geometrische Reihe
r=0.5
a=1
n=10
summe=0

#Liste zum Speichern der Terme
s_n=[]

#Berechnung der Terme und der Summe
for k in range (0, n):
    summe += a*r**k    #kummulieren
    s_n.append(summe)
    

print(s_n)

plt.plot (s_n)