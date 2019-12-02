"""
Funksionen
Eine Funkion gruppiert Anwendungen

"""
def quersumme(value):
    qs=0
    while value !=0:
        qs+=value%10
        value //=10
        
    return qs
    
print(quersumme(25333))
print(quersumme(255))
print(quersumme(252))
print(quersumme(253))
print(quersumme(2535))

# eingabe = input("Bitte zahl eingaben ")
# print(f"Die Quersumme von {eingabe} ist", quersumme( int(eingabe)))

"""    
Aufrufbar mit

q=quersumme(255)
print(q)
"""

def create_person(id, vorname, nachname):
    dict={'ID':id, 'vorname': vorname, 'nachname': nachname }
    return dict
    
liste = []
liste.append(create_person(1,'Hugo','Boss'))
liste.append(create_person(2,'Sven','Piehl'))

"""    

"""
def person_data():
    id=input('Bitte eine ID angeben ')           # Wird mit ID gefühllt
    vorname = input('Vorname eingaben ')         # Wird mit Vorname gefühllt
    nachname = input('Nachname eingeben ')       # Wird mit Nachname gefühllt
    return create_person(id,vorname,nachname)    # Weitergabe an person_data
    
liste=[]                                         # leere Liste wird erzeugt
liste.append(person_data())
print(liste)

"""    

"""

def greeting(name='User', motd='Moin'):
    print(motd, name)
preeting('Sven')
greeting('Admin','Hello')

greeting(motd='Hello')

"""    

"""

import random

def calc(v1, v2, func):
    return func(v1,v2)
print(calc(10,20,min))
print(calc(10,20,max))

def add (value1, value2):
    return value1 + value2
    
print(calc(10,20,add))
print(calc(10,random.random(),add))

"""    

"""

def swap(a,b):
    return b,a
value1=10
value2=20

value1,value2=swap(value1,value2)
print(value1,value2)

""" 
Algorithm  
Funkionen haben eine Parameterliste
0,1,2,...,n Parameter
def func
    return value # Rückgabewert
func ("""Argorente werden an eine Funkion übergeben""")
"""
