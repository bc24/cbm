"""
2.
Eine Funktion erstellen, um Binärzahlen in Dezimalzahlen umzurechnen
"""
def bin2dec(value):
    dec2=0
    x=0
    while value!=0:
        dec2=dec2+(value%10*(2**x))
        value//=10
        x+=1
    print(dec2)
ausgabe=bin2dec(int(input('Gebe eine Zahl (Binärzahl) ein: ')))

