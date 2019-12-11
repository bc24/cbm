def dec2bin( dec ):
    print( f"Umrechnung von dec2bin: Dezimalwert: {dec}" )
    print(  "Schritte: " )
    result = ""
    
    while dec != 0:
        print( f" {dec} / {2} = {dec // 2} R {dec % 2}" )
        result += str( dec % 2 )
        dec = dec // 2
    return result[::-1]

print( dec2bin( 31 ) )
print( dec2bin( 32 ) )
print( dec2bin( 15 ) )
print( dec2bin( 255 ))