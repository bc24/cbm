import sys
s = "Stehen ganz viele wichtige Informationen!"
dict_result = {}

def bubble_sort_dict( dict_list ):
    for i in range( len ( dict_list ) ):
        for j in range( len ( dict_list ) - i -1 ):
            if  dict_list[ j ][1] >  dict_list[ j + 1 ][1]:
                tmp = dict_list[ j + 1]
                dict_list[ j + 1] = dict_list[ j ]
                dict_list[ j ] = tmp
    return dict_list


for chr in s:
#    if list( dict_result.keys() ).count( chr ) == 0:
    if chr not in dict_result.keys():
        dict_result[ chr ] = 1
    else:
        dict_result[ chr ] += 1

dict_items  = dict_result.items()
item_list   = list ( dict_items )

sort_list   = bubble_sort_dict(item_list)

total_chars = len(s)

print(s)
print(f'Menge an Zeichen: {total_chars}')
for value in  sort_list[::-1][:5]:
    rel = (value[1] / total_chars) * 100
    print( f' {value[0]} kommt {value[1]:>10} mal vor {rel:>5.3f}%' )
    
