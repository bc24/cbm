def dec2bin (value):
    y=0
    s = ""
    while value!=0:
        x=0
        x=x+value%2
        s += str(x)
        print(f'{y} | {value} R {s[y]}')
        y+=1
        value//=2
    print (s[::-1])
    
ausgabe=dec2bin(int(input('Gebe eine Zahl ein: ')))