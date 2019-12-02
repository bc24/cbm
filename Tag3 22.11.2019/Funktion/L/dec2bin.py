def dec2bin( dec ):
    result = ""
    while dec != 0:
        result += str( dec % 2 )
        dec = dec // 2
    return result[::-1]
#    print(result[::-1] , "\n\n")

print( dec2bin( 31 ) )
print( dec2bin( 32 ) )
print( dec2bin( 15 ) )
print( dec2bin( 255 ))