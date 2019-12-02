"""
Eine Funktion erstellen, um aus Dezimalzahlen Hexadezimale Zahlen zu berechnen.
"""
def dec2hex (value):
    hex2=""
    while value!=0:
        x=0
        x=x+value%16
        if x==15:
            x='f'
        elif x==14:
            x='e'
        elif x==13:
            x='d'
        elif x==12:
            x='c'
        elif x==11:
            x='b'
        elif x==10:
            x='a'
        value//=16
        hex2+=str(x)
    print (hex2[::-1])
ausgabe=dec2hex(int(input('Gebe eine Zahl ein: ')))

"""
Alternative
Die kurze Fassung
"""
def dec2hex(dec):
    values="0123456789ABCDEF"
    result=""
    while dec!=0:
        result+=values[dec%16]
        dec//=16
    return result[::-1]
    
"""
Alternative
Die noch kürzere Fassung
"""
print('Nummer eingeben')
nummer=int(input())
print("Hexa Decimal ist: {0:>0x}".format(nummer))   


