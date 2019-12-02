d1 = { 'id': 1, 'vorname': 'Hantz', 'nachname': 'Banane','counter': 0}
d2 = { 'id': 2, 'vorname': 'Donald', 'nachname': 'Duck','counter': 0}
d3 = { 'id': 3, 'vorname': 'Moritz', 'nachname': 'Morning','counter': 0}

liste = [ d1,d2,d3 ]


while True:
    eingabe = input("Bitte den gesuchten Vornamen eingeben")
    if eingabe.lower() == "exit":
        break

    for eintrag in liste:
        if eintrag['vorname'] == eingabe:
            eintrag['counter'] += 1
            print( eintrag, "Anzahl der Suchvorgänge", eintrag['counter'] )
        
