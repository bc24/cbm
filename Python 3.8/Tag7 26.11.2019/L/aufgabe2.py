def read_file():
    fd = open('./cs448b_ipasn.csv', 'r')
    lines = fd.readlines()
    fd.close()
    return lines
     
def create_dict( lines ):
    dict = {}; 
    for line in lines:
        line = line.replace('\n','');
        entries = line.split(',');
        key = entries[0] + "-" + entries[1];      
        if key not in dict.keys():
            dict[ key ] = int( entries[3] );
        else: 
            dict[ key ] += int( entries[3] );           
    return dict;       
    
lines = read_file()
lines.pop(0);
dictionary  = create_dict( lines ) 
#print( dictionary );

fd = open('./results.csv', 'w')

for key, value in dictionary.items():
    #
    # 2006-07-01-7
    #   
    entries = key.split('-')
    date = entries[0] + "-" + entries[1] + "-" + entries[2] #Wegen dem Datum der Trennung mit - 
    l_ip = entries[3]
    print( f'{date};{l_ip};{value}', file=fd)

fd.close()



