'''
Arbeiten mit Dateien

'''
fd=open('Datei.txt','r')
b=fd.read(10)               #Bytes
fb.seek(0)                  #Position
                            #Return: Neue Position
fd.tell()                   #Aktuelle Position
fd.write(string)            #Schreiben der Datei
dir(fd)                     #Alle Module
fd.truncate(10)             #Datei abschneiden
fd.flush                    #Cache lerren
fd.writable()
fd.readable()
fd.seekable()
write(lines)                #Nimmt ne Liste entgegen
read(lines)                 #
fd.fileno                   # Gibt die Anzahl der geöffneten Daten aus (Eine Datei gleich 3) inport, output und Fehler Kanal

#Dateien lesen
fd.close()
fd=open('Datei.txt','r')
fd.write("Hier dein Text")

#Dateien schreiben
fd.close()
fd=open('Datei.txt','w')
fd.write("Hier dein Text")

