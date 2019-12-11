"""
Aufgaben 1
Erstelle eine Funktion und erzeuge in dieser Funktion eine Liste mit 100 Zufallszahlen.
Durchlaufe diese Liste IN EINER SCHLEIFE! und berechne die Minmal-, Maximalwer und Durchsschnitt.
"""

from random import *
liste=[]
def zz ():
    for zahl in range(100):
            zahl = random.random()    #randint(1, 100)
            liste.append(zahl)
    zahl=0
    min=1
    max=0
    return liste
    for zahl in range(0,len(liste)-1):
        
    
print(zahl) 