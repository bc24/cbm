summe = 0
hinzu=0
for x in range (0,101):
hinzu=x
    if x%3 == 0:
        summe *= 2
        hinzu=0
    if x%4 == 0:
        summe //= 3
        hinzu=0
    if x%9 == 0
        qs=0
        while summe !=0:
            qs += summe %10
        summe = qs
        hinzu=0
    summe += hinzu
print(summe)