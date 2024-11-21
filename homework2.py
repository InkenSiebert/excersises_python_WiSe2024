def buchstabe_ändern(string, buchstabe):
    string_lower=string.lower()
    
    for v in "aeiou":               #v=vokal, geht jeder index
        new_sentence=[]    #leere Liste zum Speichern
        
        for char in string_lower:           #char = Element
            if char == buchstabe:      #buchstabe, die Nutzer eingegebn hat
                new_sentence.append(v)    #ersetze v in buchstabe
            else: 
                new_sentence.append(char)
                
                
        print("".join(new_sentence))    #gleiche Ebene wie 2. for Schleife, join= zusammenführen, erst leere String starten, new_sentence zusammenführen
        
        
#buchstabe_ändern("banana", "a")

buchstabe_ändern("Wie geht es Ihnen?", "e")
