def dec2hex( dec ):
    result = ""
    while dec != 0:
        x = dec % 16
        if x == 10:
            result += "A"
        elif x == 11:
            result += "B"
        elif x == 12:
            result += "C"
        elif x == 13:
            result += "D"
        elif x == 14:
            result += "E"
        elif x == 15:
            result += "F"
        else:
            result += str( x )          
        dec //= 16
    return result[::-1]
    
print( dec2hex( 255 ) )
print( dec2hex( 256 ) )

            
            
            
            
            