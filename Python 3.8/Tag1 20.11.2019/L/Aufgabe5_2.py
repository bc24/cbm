x=0
y=0
while x<101:
    if x%3==0 and x%9==0:
        y=y+x
        while y!=0:
            y=y+y%10
            y=y//10
        x+=1
    elif x%4==0:
        y=(y+x)/3
        x+=1
    elif x%3==0:
        y=(y+x)*2
        x+=1
    else:
        y=y+x
        x+=1
print(y)