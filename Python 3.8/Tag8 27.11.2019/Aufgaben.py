# Aufagbe1
# Erstelle eine Liste mit allen Dateien im Verzeichnis Tag8/Test
import os

os.chdir(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag8")
os.listdir(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag8")

# Aufgabe2
# Summiere die Größe aller Dateien aus dem Verzeichnis Tag8
# Gebe die Summe aus
os.stat(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag8")
os.stat(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag8").st_size
for entry in os.scandir("."):
    print(entry.name, entry.is_dir())


# Aufgabe3
# Zähle alle Dateien und alle Verzeichnisse aus dem Verzeichnis Tag8/Test
# Beispielausgabe:
# Dateien: 43
# Verzeichnisse: 12
os.chdir(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag8\Test")


# Aufgabe 4
# Summiere die Größe aller Dateien in dem Verzeichnis Tag8 MIT Unterverzeichnissen

#Aufgabe langeweile
fd=open(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag8\Test\Datei.txt","w")
for entry in os.scandir("."):
    print(entry.name, entry.is_dir(), entry.stat().st_size)
    
    if entry.is_file():
        print("Die Größe der Datei ",entry.name, entry.stat().st_size, file=fd)
   
    