# Ausnahmebehandundlung (Exception)
# Zum Abfragen von Fehlern in Programmen

    #Fehler
    i=10
    x=0
    result=i/x

#Immer Zusammen
try except
try finally
try except finally


try()               # Fehler wird übersprungen #Nur in der "Immer Zusammen" Kobi
except()            # Ausgabe trotz Fehler
raise()             # Kann immer auftretten

#raise Beispiel
x = "hallo"
if not type(x) is int:
  raise TypeError("Fehlermeldung")
  


#Beispiel 1
try:
    15/0
finally:
    print("Blub")

#Beispiel 2
try:
    15/0
except Fehler:
    fd=open("error.log","w")
    print("Teilung durch 0", file=fd)
    fd.close()
    raise

#Beispiel 3
def Test():
    eingabe=input("fghjuiopü")
    try:
        value=float(eingabe)
        print(f'blaaaaaaaa von Value^2 {value**2}')
        break
    except ValueError:
        print("Fehler: dfcghjklö")
Test()

#Eingabe eines einzelnen Zeichens
import msvcrt

#Beispiel
while True:
    c = msvcrt.getch()
    if c==b 'q':
        break
    print(c,end=")