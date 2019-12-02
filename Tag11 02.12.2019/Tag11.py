# eneratoren
# Das yield Schlüsselwort erzeugt einen Generator/Iterator
#2  4   8   16  32  64  128 512 1024    2048

def power():
    value = 1
    while True:
        value +=1
        yield 2**value
x=power()
next(x)

# Beispiel1
#x=power()
#for i in range(10):
#    power(next(x))
#print(next(x))

# Beispiel2
def fibo (max):
    a=0
    b=1
    for x in range(max):
        c=a+b
        a=b
        b=c
        yield c

list(fibo(20))

#Eingebauter Generator
import os
x=os.scandir(".")

# Hashwerte
# hash(object)
import hashlib              # hashlib inportieren
dir(hashlib)                #
sha512.update(b"test")      #
sha512.hexdigest()          #
print(hashlib.sha3_512(b"Bannane").hexdigest())


#