x=100
y=0
while x>0:
    if x%3==0 and (x/3)%2==1:
        y=y+x
        x-=1
    else:
        x-=1
print(y)