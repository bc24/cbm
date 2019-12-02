def read_file():
    fd = open('cs448b_ipasn.csv', 'r')
    lines = fd.readlines()
    fd.close()
    return lines
     
def create_dict( lines ):
    dict = {}; 
    for line in lines:
        line = line.replace('\n','');
        entries = line.split(',');      
        if entries[0] not in dict.keys():
            dict[ entries[0] ] = int( entries[3] );
        else: 
            dict[ entries[0] ] += int( entries[3] );           
    return dict;       
    
lines = read_file()
lines.pop(0);
dictionary  = create_dict( lines ) 
#print( dictionary );

fd = open('results.csv', 'w')

for key, value in dictionary.items():
    print( f'{key};{value}', file=fd)

fd.close()



