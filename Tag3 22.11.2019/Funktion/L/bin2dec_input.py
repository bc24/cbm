#
# Aufbabenblatt 2 
# Aufgabe 1
#  
# 
  
def bin2dec( bin ):
    dec = 0
    factor = 0
    
    for v in bin[::-1]:
        dec += int( v ) * 2**factor
        factor += 1
    return dec
    
	
print( bin2dec( input("Bitte Binärzahl eingeben" )  ) )
