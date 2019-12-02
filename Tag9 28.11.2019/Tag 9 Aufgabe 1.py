print ("Drücke W,A,S,D um dich zu bewegen:")
Liste=[[0,1,2],[3,4,5],[6,7,8]]
col=0
row=0
while True:
    for y in range(len(Liste)):
        for x in range(len(Liste[y])):
            if x==col and y==row:
                print('x',end=" ")
            else:
                print(Liste[y][x],end=" ")
        print(" ")
    inp = input()
    if inp =="d":
        col+=1
        if col>2:
            print("geht nicht")
            col-=1
            print(" ")
    elif inp =="a":
        col-=1
        if col<0:
            print("geht nicht")
            col+=1
            print(" ")
    elif inp =="s":
        row+=1
        if row>2:
            print("geht nicht")
            row-=1
            print(" ")
    elif inp =="w":
        row-=1
        if row<0:
            print("geht nicht")
            row+=1
            print(" ")





