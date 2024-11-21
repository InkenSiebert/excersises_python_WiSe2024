
a=1
r=0.5
s=0
k=0
limit =a/(1-r)     # 
epsilon=0.001      #Abstand möglichst klein





while True:
    s+=a*r**k
    k+=1
    print(s,end=" ")
    if (limit -s)< epsilon:
        break
    
    #unsaubere Lösung 

      #   if s==(a/(1-r)):
        # break
