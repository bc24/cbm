'''
 Woche 3
 Bit-Flaggen
 Eigene Module entwickeln
 HTTP / HTTPS Client/Server
 Vieleicht: Hashwerte und Koodierung
 Farbliche Gestaltung der Konsole
 Do: Wiederholungen
 Fr: Klausur
'''
# SQLite
# Datenbankensystem
# ********


import sqlite3
ver=sqlite3.connect('DatenbankName')        # Datenbank verbindung erstellen
cur=ver.cursor()                            # Den Cursor zum Arbeiten holen
res=cur.execute('Select 1')                 # Einzelne Anweisung
print(res.fetchall())
#---------------------------------------
res=cur.execute('select "Hallo","blub"')
#---------------------------------------
res=cur.execute('select 1+1')
print(res.fetchall())
#---------------------------------------
# cur.executescript("""create table Person(vorname,nachname)""")                # Tabelle anlegen
# cur.executescript("""create table adresse(str,plz,ort)""")
# cur.execute("""insert into Person values("Hans","Mueller")""")                # Tabelle füllen
# res=cur.execute("""select * from Person where vorname'" + vorname +'""")      # Abfrage von Person -> Vorname

#Prepared Statements
# %s
# {}
#db.execute("INSERT INTO Person (vorname, nachname) VALUES (?, ?)", ("Mc", "Donald")
#  ___________________
# |SQLite Datentypen  |
# |-------------------|
# |Text               |
# |int                |
# |real               |
# |blob               |
# |date               |
# |___________________|

#rollback
# ver.commit()    # Nach dem Commit werden alle Änderungen übernommen
# ver.close()     # Beendet die Datenbankverbinung

#Beispiel 1
# query="""(create table Autos(id integer primary key autoincreme) marke Text, doors int,ccm int)""")
# cur.execute("""insert into Autos(marke,doors,ssm)values('Testla',7,0)""")
