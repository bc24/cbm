#
#Blatt 1 Aufgabe 4
#

value = 255
qs = 0

while value != 0:
	qs += value % 10
	value //= 10
	
print("Die Quersumme: " , qs)