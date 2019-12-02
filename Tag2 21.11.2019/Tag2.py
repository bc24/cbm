#Strings
#String                         Beispiel                Beschreibung
s.lower                         s="Hallo Welt"          # Weißt das s denn Wert Hallo Welt zu
s.lower()                       s.lower(Hallo)          # lower gibt alles klein aus
s.upper()                       s.upper(Hallo)          # upper gibt alles groß aus
s.swapcase()                    s.swapcase(Hallo        # Gibt alles was klein ist groß aus und andersrum
s.startswith()                  s.startswith(Hallo)     # swapcase gibt alles groß aus
"hallo welt".capitalize()                               # Erster Buchstabe groß geschrieben
s.find()                        s.find('elt')           # Sucht in welchen Index das elt sich befindet
s[0]                                                    # Gibt den Index 0 aus (H)
s[0:-1]                                                 # Gibt den Index 0 bis -1 aus (Hallo Wel)
s[:-1]                                                  # Der : ersetzt die 0
s[::-1]                                                 # Das doppelte :: Gibt den Wert andersrum aus
x="abc def ghi jkl mno"                                 #
s.split(" ")                                            #
s.splitlines()                                          #
s = input()                 v= input("Deine Paypal")    #
s.count()                   s.count("em")               # 

#Aufgaben String
# Frage vom Benutzer eine E-Mail-Adresse ab.
# Prüfe, ob sich ein "@" Zeichen in der Adresse befindet, ob die Domain mindestens einen Punkt hat und ob der Benutzername aus mindestens einem Zeichen besteht.
# Ist dies nicht der Fall, verlange eine erneute Eingabe.
# Ist alles richtig, bestätige die E-Mail-Adresse mit einer Ausgabe.

Benutzer = input("Bitte gebe deine E-Mail Adresse ein: ")
if Benutzer.count('.') and Benutzer.count('@')>0:
    print(Ihre E-Mail Adresse lautet:, Benutzer)
        else import("Sie haben keine gültige E-Mail Adresse angegeben, bitte geben Sie Ihre E-Mail Adresse erneut ein: ")


#Listen
#Listen                         Beispiel                Beschreibung
list[]                          liste = [3,6,8]             #
.append                         liste.append                # Fügt am ende der Liste etwas hinzu
.count                          liste.count                 # 
.reverse                        liste.reverse               #
.insert                         liste.insert                # 
.pop                            liste.pop                   # Bei nit angabe wird der letzter listen eintrag gelöscht
.copy                           liste.copy                  # Tiefe Kopie

#pop Beispiel
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.pop()
print ("list now : ", list1)

list1.pop(1)
print ("list now : ", list1)

#Aufgaben Liste
# Erstelle eine Schleife. 
# Fordere den Benutzer auf eine Zeichenkette einzugeben. 
# Speichere die Zeichenkette in einer Liste.
# Gibt der Benutzer das Wort "exit" ein, dann beende die Schleife. 
# ( Zum Abbrechen einer Schleife verwenden wir break )
# Gibt der Benutzer das Wort "print" ein, gebe alle Listeneinträge aus.

Benutzer = input("Gebe eine Zeichenkette ein: ")
BenutzerListe = [Benutzer]
if Benutzer.count('exit') >True:
    break;
if Benutzer.count('print')>True:
    elif print(BenutzerListe)
    
Benutzer=[]
while true:
    Eingabe=input("Gebe irgendwas ein: ")
    liste.append(Benutzer)
    if Benutzer==('exit'):
        break;  


#Dictionaries
#Dictionaries                         Beispiel                Beschreibung
Key : value
                                    d['Apfel']
                                    d.update(d2)
                                    d.get(0)   # Das gleich wie d[0]
                                    d.fromkeys(liste)
                                    v= d.pop('Apfel') #Birne
                                    del d['Apfel']
                                    
                                    #Beispiel:
                                    person = {'firstname': 'John', 'lastname' : 'Doe' , 'Country' : "NK"}
                                    person['firstname']
                                    liste=[person]
                                    liste[0]
.keys()
.values()

# Aufgaben 1
# Erstelle eine Liste mit 3 Dictionaries.
# Jedes Dictionary ist gleich aufgebaut. 
# Die Keys sind ID, Vorname, Nachname
# Die Values denkt euch selbst aus.
# Frage vom Benutzer einen Vornamen ab. Suche in der Liste das Dictionary mit dem Vornamen und gebe dies aus.

Liste =	{
  "ID": '1','2','3'
  "Vorname": "Jan", "Miriam", "Florian"
  "Nachname": "Mueller", "Schmidt", "Meyer"
}

x = Liste["Liste"]
x = Liste.get("Liste")

for x in Liste:
  print(Liste[x])
  
# Aufgaben 2
# Erstelle eine Statistik über deine Abfrage
# Führe die Abfrage des Benutzernamens in einer Schleife aus. 
# Speichere, wie häufig eine Person gesucht wurde. Gebe mit jeder Ausgabe die Anzahl der Personensuche mit aus.


  

#Tuple
#Tuple                         Beispiel                Beschreibung
bla=(1,2,3,4,5,6,7)
bla.count(5)
tuple                           tuple 'Moin Bremen'






#Sets