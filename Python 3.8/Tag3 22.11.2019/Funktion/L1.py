def dec2bin(value):
    if value == 0:
        return ""
    return str(dec2bin(value//2))+str(value%2)
   