import msvcrt
import sys
import os

def print_list( liste, row, col ):
    for y in range( len( liste ) ):
        for x in range( len( liste[0] ) ):
            if y == row and x == col:
                print('x' , end=' ')
            else:
                print( liste[y][x], end=' ')
        print('')
        

liste =  [ [ 0 , 1, 2] , [ 3, 4, 5] , [ 6, 7, 8] ]
#liste =  [ [ 'o' , 'o', 'o'] , [ 'o', 'o', 'o'] , [ 'o', 'o', 'o'] ]

row = 0
col = 0

#print_list( liste, 1,1)
#print_list( liste, 2,1)
#print_list( liste, 0,0)
#sys.exit(0)


while True:
    os.system("cls")
    print_list( liste, row, col)

    chr = msvcrt.getch()
    
   
    if chr == b'q':
        print("Bye")
        sys.exit(0)
        
    elif chr == b'd':       
        if col+1 < len( liste[ row ] ):
            col += 1
    
    elif chr == b'a' and col > 0:
        col -= 1
        
        
    elif chr == b'w' and row > 0:
        row -= 1
    
    elif chr == b's':
        if row + 1 < len ( liste ):
            row += 1
