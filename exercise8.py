def vokon_zählen(x): 
    vokale = ["a", "e", "i", "o" "u"]    #"aeiou"
    x_lower=x.lower()
    
    buchstaben=[i for i in x_lower if i.isalpha()]   #Buchstaben speichern aus x_lower
    vokale=[i for i in buchstaben if i in vokale]
   
   #return [len(buchstaben), len(vokale)]
print(f"Es gibt {len(vokale)} Vokale und {len(buchstaben)- len(vokale)} Konsonanten.")  

#print(vokon_zählen("HalIU+#§o, Berlin!"))  

vokon_zählen("Halllo, &%/ BerliN!!")