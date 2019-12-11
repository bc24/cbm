
#**********************************************************************************************************************
# Aufgabe 1
# Mit Python eine SQLITE3 Datenbank erstellen. Die Datenbank benötigt die Felder
# date, l_ip, r_asn, flows
# Fülle die Datenbank jetzt mit den Werten aus der csv Datei "cs448b_ipasn.csv"
# Das DATE Feld sollte den Datentypen TEXT nutzen
#**********************************************************************************************************************

import csv, sqlite3, os, sys

con = sqlite3.connect("Datenbank-29.11.2019.2")
cur = con.cursor()

cur.execute("DROP TABLE Datenbank")
cur.execute("CREATE TABLE Datenbank(data,l_ip,r_asn,flows)")

fd = open(r"H:\Fächer\Programmierung mit Python\Uebungen\Tag10 29.11.2019\cs448b_ipasn.csv" , "r");
lines = fd.readlines()

for line in lines:
    line = line.replace("\n","")
    items = line.split(",")
    to_db= tuple(items)
    cur.execute("INSERT INTO Datenbank (data, l_ip, r_asn, flows) VALUES (?, ?, ?, ?);", to_db)

con.commit()
con.close()

#**********************************************************************************************************************
# Aufgabe 2
# Erstelle ein neues Programm und verlange vom Benutzer die Eingabe eines Datums: Finde zu dem Datum aus der
# Datenbank alle Werte und gebe diese mit Angabe der Gesamtzahl aus.
# z.B.
# Datum: 2006-07-01
# Einträge: 4
#
# LocalIP: 0, ASN:        701,     Flows:     1
# LocalIP: 0, ASN:        714,     Flows:     1
# LocalIP: 0, ASN:      1239,     Flows:     1
# LocalIP: 0, ASN:      1680,     Flows:     1
#**********************************************************************************************************************
res = cur.execute("select * from Datenbank where date>2018-11-29")
print(res.fetchall())
def Datum_Ausgabe(res):
    eingabe = input("Bitte gebe eine Datum ein: ")
    for i in range(len(sys.argv)):
        if i == 0:
            print("Datum: %s" % sys.argv[0])
        else:
            print("Einträge: %s" % (i,sys.argv[i]))

    return liste
    liste[]
print(liste=[/n,/t]