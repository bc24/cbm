def dec2bin( dec ):
    result = ""
    while dec != 0:
        result += str( dec % 2 )
        dec = dec // 2
    return result[::-1]


bin = dec2bin( 255 )

res = 0

for chr in bin:
	if chr == "1":
		res += 1

print(f'Der Wert {bin} hat {res} 1en')