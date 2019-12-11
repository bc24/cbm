"""
Aufgabe 4
Schreibe ein Programm welches Kommandozeilenargumente entgegennimmt, diese als Listenelemente
speichert und dann, sortiert nach der Länge der Argumente ausgibt.
Beispiel
programm.py ab cde klmnx fghi

Ausgabe
ab 
cde
fghi
klmnx 
"""
from sys import *
from os import *

def Kommandozeilenargumente(fun):
    for i in range(len(sys.argv)):
        if i == 0:
            print "Funktionsname: %s" % sys.argv[0]
        else:
            print "%d. Argument: %s" % (i,sys.argv[i])

    return liste
    liste[]
print(liste=[/n,/t]







"""
Mit einbauen
***************
 os.chdir(path)
 sys.path
  """