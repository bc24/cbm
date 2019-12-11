
Definiere die Eigenschaften als BitFlags:
    user_active
    user_suspended
    user_can_change_passwd
    user_has_premium
    user_has_admin_privileges


Schreibe jetzt Funktionen um einen Wert des Benutzers zu setzen, zu ändern oder zu prüfen

    set_flag
    unset_flag
    has_flag
    toggle_flag

********************************************************************************************************************

import os
import stat

user_active =                   0x001
user_suspended =                0x002
user_can_change_passwd =        0x004
user_has_premium =              0x008
user_has_admin_privileges =     0x010
                            #--------------------
user =                             31


def set_flag(user,value):
    return user|value

def unset_flag(user,value):
    return user & value

def has_flag(user,value):
    return user | value

def toggle_flag(user,value):
    return user^value

def test():
    user=0
    user=user_active(user,user_active)
    user=toggle_flag(user,user_has_premium)
    user=print(has_flag(user,user_active) and has_flag(user,user_has_premium))

********************************************************************************************************************
Aufgabe 2
Füge der Datenbank eine neue Tabelle hinzu. Generiere zufällige Werte bis (maxvalue) und trage diese in der Tabelle ein
maxvalue = user_active | user_suspended | user_can_change_passwd | user_has_premium |user_has_admin_privileges
********************************************************************************************************************
import csv, sqlite3, os, sys

con = sqlite3.connect("Tag12")
cur = con.cursor()

cur.execute("DROP TABLE Tag12")
cur.execute("CREATE TABLE Tag12(user_active,user_suspended,user_can_change_passwd,user_has_premium,user_has_admin_privileges)")

fd = open(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag11 02.12.2019\MOCK_DATA_PERSON.csv" , "r")
lines = fd.readlines()

def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password

for line in lines:
    line = line.replace("\n","")
    items = line.split(",")
    items[2] = hash_generierung

    to_db= tuple(items)
    cur.execute("INSERT INTO Datenbank (user_active,user_suspended,user_can_change_passwd,user_has_premium,user_has_admin_privileges) VALUES (?, ?, ?, ?, ?);", to_db)


con.commit()
con.close()

********************************************************************************************************************
Aufgabe 3
Schreibe ein Programm, frage nach einer E-Mail-Adresse und geben dann den Benutzer aus der Datenbank mit allen Daten an.
Beispiel für die Suche nach ddownton0@disqus.com

Vorname:		Dareen
Nachname: 		Downton
E-Mail:			ddownton0@disqus.com
Passwort: 		Super Toller SHA512 Wert
IP: 			96.133.79.218
CC: 			374622698695276
Uservalue: 		6 [suspended, can_change_passwd]
********************************************************************************************************************

import sqlite3, os, sys, socket

print("Bitte fülle alle Felder aus: ")
vorname=input("Vorname: ")
nachname=input("Nachname: ")
email=input("E-Mail: ")
passwort=input("Passwort: ")
ip = os.popen('hostname -I').readlines()
cc=input("Bitte gebe CC an: ")
user=input("Username: ")
uservalue=input()

Print("Bitte Kontrolieren Sie Ihre Daten")
print(vorname)
print(nachname)
print(email)
print(passwort)
print("Ihre IP-Adresse lautet " + " ".join(IPAdresse) + ".")
print(cc)
print(user)
print(uservalue)

con = sqlite3.connect("Tag12-aufgabe3")
cur = con.cursor()

cur.execute("DROP TABLE Tag12-aufgabe3")
cur.execute("CREATE TABLE Tag12-aufgabe3(vorname,nachname,email,passwort,ip,cc,user,uservalue)")

    #to_db= tuple(items)
    cur.execute("INSERT INTO Datenbank (vorname,nachname,email,passwort,ip,cc,user,uservalue) VALUES (?, ?, ?, ?, ?, ?, ?, ?);", to_db)


con.commit()
con.close()