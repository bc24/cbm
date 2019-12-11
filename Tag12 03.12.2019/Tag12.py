# Bit-Flaggen
#### Tafel ####

readable = 0x1          # 001
writable = 0x2          # 002
executable = 0x4        # 003

rw = readable|writable  # 01'

if rw&writable !=0:
    print("writable")

rw | = executable   # 111

rw = (rw|readable)^readable     # OFF


rw = ^=readable # Immer an und aus
rw = °=readable

&           check
|           set
^           Toggle
..|..^      UNet

'''
Wahrheitstabellen    
 011
&010
-----
 010
 
 011
&100
-----
 000
'''

### Console ####

#Beispiel
import os
import stat                     #dir(stat)
stat.FILE_ATTRIBUTE_ARCHIVE #2
stat.FILE_ATTRIBUTE_ARCHIVE #32
stat.FILE_ATTRIBUTE_SYSTEM  #4
stat.FILE_ATTRIBUTE_DIRECTORY   #16

for name in dir(stat):
    if name[0] == 'F':
        print(name,getattr(stat,name))

R=0x001
W=0x002
E=0x004

value=R|W
value           #3

value & R !=0   #True

value & E !=0
value           #7

value&E!=0      #True

value =(value | E)^E
value           #3

value=(value|E)^E
value           #3

value=value^E
value           #3

value=value|E
value           #7

value=R|W
value       #3
#toggeln
value=(value | R) ^ R   # Ein und aus schalten
