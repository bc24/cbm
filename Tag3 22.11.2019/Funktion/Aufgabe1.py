"""
1.
Schreibe eine Funktion: Die Funktion hat einen Parameter mit dem Bezeichner dec,
Berechte aus dem Dezimalwert dec den Binärwert NATÜRLICH ohne die eingebauten
Funktionen bin hex und so weiter.
"""
n=int(input('Gebe eine Zahl ein: '))
x=n
k=[]
def umrechnen(n)
    while (n>0):
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2
    k.append(0)
    string=""
    for j in k[::-1]:
        string=string+str(j)
    print('Die Binärzahl aus %d lautet %s'%(x, string))
