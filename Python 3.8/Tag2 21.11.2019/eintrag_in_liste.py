liste = []
while True:
    line = input("Ihre Eingabe: ")
    
    if line.lower() == "exit":
        break
    if line.lower() == "print":
        for row in liste:
            print( "Eintrag: " , row )
      
    liste.append( line )