# Themen der Wiederholung
### Arbeiten mit Dateien Verzeichnissen
# Daten
# Wir mit open geöffnet
#  Wir erhalten eine File Descripter
#                    ===============
#                               | read(Bytes)                   - liest wie groß die Datei ist
#                               | readlines()                   - liesst alle Zeilen aus
#                               | write(String)                 - schreibt einen String in die Datei
#                               | writelines(liste)             - schreibt in die Liste
#                               | tell()                        - Wo befindet sich der curser
#                               | seek(pos,startrichtung)       - gibt die aktuelle Posision aus
#                               | truncate(NeueGröße)           - ?
#                               | flush()                       - leert der Cache und schreibt es in die Datei
#                               | close()                       - schließt das Script
#
# read, write, append, r+, w+
#  |      |      |     |   |
#  -------------------------
#         Write only

#### Arbeiten mit Verzeichnissse (OS Modul)
# import os                                 # Inport des Modul os
# os.getcwd()                               # Ausgabe von Aktuellen Verzeichnis
# os.chdir("../")                           # In einen Verzeichnis
# os.mkdir("test")                          # Verzeichnis anlegen
# #os.rmdir("../../../Windows/System32 *")  # Löschen von Verzeichnis
# os.listdir("./")                          # Auflisten von allen Dateien in einen Verzeichnis
# os.stat('Datei.blub')                     # Infos der Datei
#                                             time.asctime()
#                                             time.localtine()
# os.listdir()                              # Alle Verzeichnis Elemente auflisten
# os.rename(AlterName,NeuerName)            # Umbenenen von einen Ordner/Datei
# os.scandir(.)                             # Erweiterung von os.listdir()
# os.unlink("Datei_zum_Löschen")            # Löscht Datei
#
#
## Exceptions (try, except,raise, finally)
# Beispiel 1:

# try:
#   15/0
# except ZeroDivionError as err:
#   print(typeError)
#   print(err.args)

# Beispiel 2
# try:
#     15/0
# finally:
#     print('year')

# Klausur Frage
try:
    print("1")
    15/0
    print("2")
finally:
        print("3")

# Ergebniss 1 und 3

# Windows kack
import msvcrt
while True:
    chr=msvcrt.getch()
    if chr == b'q':
        break
    else:
        print(chr)

