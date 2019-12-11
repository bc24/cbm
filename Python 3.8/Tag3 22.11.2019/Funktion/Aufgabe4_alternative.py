def dec2hex(dec):
    values="0123456789ABCDEF"
    result=""
    while dec!=0:
        result+=values[dec%16]
        dec//=16
    return result[::-1]