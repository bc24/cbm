summe = 0
x=0
for x in range (0,101):
    if x%3 == 0:
        summe *= 2
        x+=1        
    elif x % 4 == 0:
        summe /= 3
        x+=1        
    elif x % 9  == 0:
        summe = summe+x%10
        summe=summe//10
        x+=1
    else:
        summe=summe+x
        x+=1
print(summe)