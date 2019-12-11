'''
Aufgabe 1
Erstelle einen String mit einem beliebigen Satz (kann ruhig ein längerer sein).
Zähle alle Zeichen in dem Satz und gebe die 5 häufigsten Buchstabenvorkommen, mit
Angabe der absoluten und relativen Häufigkeit (%) aus.
'''

import string
d = {}
Satz="Die oft lustigen Sätze können bewertet und per Link z.B. über soziale Netzwerke, Instant-Messanger oder E-Mail geteilt werden. Auch eine Rangliste mit den besten, schlechtesten oder neusten Sätzen ist vorhanden. Für jede Art von Lob und Kritik gibt es das Feedback-Formular. Wenn dir z.B. ein grammatikalischer Fehler bei einem Satz auffällt, kannst du ihn schnell an den Entwickler weiterleiten und damit zur Verbesserung des Satzgenerators beitragen."
count = 0
print(len(Satz))        #452
liste = list(Satz)
for char in Satz:
  if list(d.keys()).count(char) == 0:
    d[char] = 1
  else:
    d[char] += 1
  
print(d)


