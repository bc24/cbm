'''
Dictionary Wiederholung

Dictionaries sind Key/Value Paare
'''

dict[5]="Fünf"
dict[3]="Drei"
dict[(0,1)]="Null, Eins"
dict[(0.1)]="NullKommaEins"
dict
{5:'Fünf',3:'Drei',(0,1):'Null,Eins',0.1:'NullKommaEins'}
(0,1) in dict.Keys()
dict['liste'][5]
dict[5]
sizedict={'kibi':'2**10','mebi':'2**20','gibi':'2**30'}
dict['sizes']['mebi']
dict['sizes']['gibi']
dict['sizes']['gibi']
print(545435375465465 / dict['sizes']['gibi'],"gb")
print(565656356353566 / dict['sizes']['gibi'],"gb")
dict.keys() 
dict.values()
dict.values()
list(dict.items())
for key,value in dict.items():
    print(key,value)
    
#Update
dict={'a':'5','b':'19','c':'27'}
dict.update{'c':'99','d':'127','e':'1'}

dict.update(dict_update)
dict
dict_update

#Noch mal
dictA={'a':'5','b':'19','c':'27'}
dictB{'c':'99','d':'127','e':'1'}

dictA
dictB

'''*****************************
Arbeiten mit Verzeichnise
Alle notwenigige Funksionen  finden wir im Modukl os
'''
import os   #Inport des Modul os
os.getcwd()   #Ausgabe von Aktuellen Verzeichnis
os.chdir("../") #In einen Verzeichnis 
os.mkdir("test") # Verzeichnis anlegen
#os.rmdir("../../../Windows/System32 *") #Löschen von Verzeichnis
os.listdir("./") # Auflisten von allen Dateien in einen Verzeichnis
os.stat('Datei.blub') #Infos der Datei
os.listdir()    #Alle Verzeichnis Elemente auflisten
os.rename(AlterName,NeuerName) # Umbennen von einenn Ordner
os.scandir(.)   #

'''
______________
DirEnty       |
______________|
Name :String  |
______________|
is_dir(): bool|
is_file() bool|
stat() :stat  |
______________|
'''
os.unlink(Verzeichnis/Datei)  #Löschen einer Datei


#Beispiel
os.mkdir("Test")                #Test Verzeichnis anlegen
os.chdir("Test")                #Ins Verzeichnis gehen
fd=open("Datei.txt","w")        #Datei.txt anlegen
print("Ganz viel Text",file=fd) #Text in die Datei.txt schreiben
fd.write("Super Text\n")        #Text mit Zeilenumbruch
fd.close()                      #Datei schließen
os.unline("Datei.txt")          #Löschen der Datei.txt
os.chdir("..")                  #In das da rüberliegende Verzeichnis gehen
os.rmdir("Test")                #Löschen der Verzeichnis Test

