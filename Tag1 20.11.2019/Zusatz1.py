#Zusatz 1
value=255
def Quersumme(value):
    result = 0
    while value:
        result += value % 10
        value = int(value / 10)
    return result

while True:
    eingabe = rawinput("value")
    if not eingabe: 
        break
    intzahl = int(eingabe)
    q = Quersumme(intzahl)
    print "Die Quersumme von %i  ist: %i" % (intzahl, q)
    print
	
	value = 255
quersumme = sum([int(i) for i in str(value)])


