d1 = { 'id': 1, 'vorname': 'Hantz', 'nachname': 'Banane'}
d2 = { 'id': 2, 'vorname': 'Donald', 'nachname': 'Duck'}
d3 = { 'id': 3, 'vorname': 'Moritz', 'nachname': 'Morning'}

liste = [ d1,d2,d3 ]


eingabe = input("Bitte den gesuchten Vornamen eingeben")

for eintrag in liste:
    if eintrag['vorname'] == eingabe:
        print( eintrag )
        
