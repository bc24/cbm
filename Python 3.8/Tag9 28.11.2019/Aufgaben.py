'''
Aufgabe 1
*********
Erstelle eine mehrdimensionale Liste mit den Werten
liste =  [ [ 0 , 1, 2] , [ 3, 4, 5] , [ 6, 7, 8] ]

Nutzte den Code von der Tafel um einen Buchstaben vom Benutzer abzufragen.
Ist die Benutzereingabe ein "q", dann breche das Programm ab ( sys.exit(0) )
Gebe die aktuelle Position in der Liste aus (wir fangen oben links an)
Ausgabe: Zeichnung 1
Gibt der Benutzer ein "s" ein, navigiere nach unten
Ausgabe: Zeichnung 2
Gibt der Benutzer ein "d" ein, navigiere nach rechts

Aufgabe 2
*********
Füge zu deinem Programm jetzt Exceptions hinzu. Verhindere, dass sich der Benutzer
außerhalb der Listengrenzen bewegt. Füge eine Fehlermeldung hinzu: Hier geht es
nicht weiter…


Steuerung
*********
A   <-
D   ->
W   ^
S   v
Zeichnung 1      Zeichnung 2      Zeichnung 3
 _______         _______         _______
| x,1,2 |   D   | o,x,2 |  S    | o,1,2 |
| 3,4,5 |       | 3,4,5 |       | 3,x,5 |
| 6,7,8 |       | 6,7,8 |       | 6,7,8 |
|_______|       |_______|       |_______|

Nachlesen auf https://docs.python.org/3/tutorial/errors.html
****************************************************************************
'''
import msvcrt, os

liste=[[0,1,2],[3,4,5],[6,7,8]]

col=0
row=0

while True:
    eingabe=input("Bitte gebe A=Links,D=Rechts,W=Hoch,S=Unter oder Q zum Beenden ein:" ) 
    for y in range(len(liste)):
        for x in range(len(liste[y])):
            if x==col and y==row:
                print(x,end=" ")
            else:
                print(liste[y][x],end=" ")
                  
    if eingabe == "a":
        col-=1
        if col>2:
                
            break
        print(" ")
            
    if eingabe == "d":
        col-=1
        if col>0:
                
            break
        print(" ")    
            
    if eingabe == "w":
        col-=1
        if col>2:
                
            break
        print(" ")
           
    if eingabe == "s":
        col-=1
        if col1>0:
                
            break
        print(" ")    

    if eingabe == "q":
        break
        
        
# Aktuelles Datum        
# time.asctine(time.localtime(s.st_ctime))