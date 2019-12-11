import sys

def quersumme(value):
    qs=0
    while value !=0:
        qs+=value%10
        value //=10
        
    return qs
    
print(quersumme(25333))
print(quersumme(255))
print(quersumme(252))
print(quersumme(253))
print(quersumme(2535))

eingabe = input("Bitte zahl eingaben ")
print(f"Die Quersumme von {eingabe} ist", quersumme( int(eingabe)))
