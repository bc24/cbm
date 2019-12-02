# Aufgabe 1
#**************************************************************************************************************************
# Erstelle ein Modul, welches dir eine Funktion zur Verfügung stellt, mit derer aus einer Datei ein Hashwert generiert    |
# wird. Der Funktionskopf soll dabei so aussehen:                                                                         |
# def  file_to_sha512( filename )                                                                                         |
# Die Funktion soll am Ende den lesbaren SHA512 Hashwert zurückgeben. Verhindere, dass jemand das Modul direkt ausführt.  |
#**************************************************************************************************************************
"""
import hashlib

file = ".\Datei.txt"
BLOCK_SIZE = 65536

file_hash = hashlib.sha256()
with open(file, 'rb') as f:
    fb = f.read(BLOCK_SIZE)                         # e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    while len(fb) > 0:
        file_hash.update(fb)
        fb = f.read(BLOCK_SIZE)

print (file_hash.hexdigest())

"""
# Aufgabe 2
#**************************************************************************************************************************
# Erweitere dein Modul um eine Funktion                                                                                   |
# def file_check_sha512( filename, hash )                                                                                 |
# Ist der Wert von (hash) mit dem generierten Hashwert identisch, dann gebe True zurück                                   |
#**************************************************************************************************************************

import hashlib

file1 = ".\Datei1.txt"
file2 = ".\Datei2.txt"
BLOCK_SIZE = 65536

file_hash = hashlib.sha256()
with open(file1 and file2, 'rb') as f:              # Datei 1
    fb = f.read(BLOCK_SIZE)                         # e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    while len(fb) > 0:                              # Datei 2
        file_hash.update(fb)                        # e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
        fb = f.read(BLOCK_SIZE)

print (file_hash.hexdigest())

# Aufgabe 3
#**************************************************************************************************************************
# Finde heraus, welche 3 Wörter sich in SHA verstecken                                                                    |
#**************************************************************************************************************************
#   S   = Secure
#   H   = Hash
#   A   = Algorithm