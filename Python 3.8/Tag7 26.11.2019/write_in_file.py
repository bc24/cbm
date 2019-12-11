#
# M$ Variante mit einem String ohne "Escape" Zeichen
#
fd = open(r'c:\users\svenp\desktop\dateiname.txt', 'w')

#
# M$ Variante mit "escapten" Backslashes
#
#fd = open('c:\\users\\svenp\\desktop\\dateiname.txt', 'w')

#
# *NIX Variante
#
#fd = open('c:/users/svenp/desktop/dateiname.txt', 'w')

print("Eine tolle Zeile", file=fd)

fd.close()