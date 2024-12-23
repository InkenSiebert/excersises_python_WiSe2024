import matplotlib.pyplot as plt

def buchstaben_häufigkeit(x):   #Eingabe (Input)
    mein_dic = {}
    
    for b in x.lower():
        if b.isalpha(): 
            if b not in mein_dic:
                mein_dic[b] = 1 #speicher Buchstabe in Dictionary, Eintrag in dictionary
            else: 
                mein_dic[b]+=1 #Buchstabe existiert schon. addiere 1
                
                
    mein_dic_sorted = dict(sorted(mein_dic.items()))

    return mein_dic_sorted   #Ende der Funktion, Funktion wird programmiert, return immer am Ende der Funkton

bh_dict=(buchstaben_häufigkeit(x="123Wie geht es Ihnen%$?"))  #speichert Ausgabe in einem Dictionary,   außerhalb der Funktion
bh_dict2=(buchstaben_häufigkeit(x="Hallo, Berlin123"))

#buchstaben_häufigkeit(x="Hallo, Berlin123") Funktion gibt nichts zurück, Werte werden nicht gespeichert mit print wird es gezeigt, aber nicht gespeichert
                                                #Return funktioniert nur in der Funktion
#plt.bar(bh_dict.keys(), bh_dict.values())


plt.bar(bh_dict2.keys(), bh_dict2.values())
