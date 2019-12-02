d1={'id' : '1' , 'Vorname' : 'Hans', 'Lastname' : 'Banane'}
d2={'id' : '2' , 'Vorname' : 'Dieter', 'Lastname' : 'Mueller'}
d3={'id' : '3' , 'Vorname' : 'Joline', 'Lastname' : 'Harjes'}
list = [d1, d2, d3]
Benutzer = input("Geben sie bitte Ihre Name: ")

for x in list:
	if x ['vorname'] == Benutzer :
		print(x)
