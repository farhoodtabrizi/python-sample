def find_word_vertical(crosswords,word):
    z=[list(i) for i in zip(*crosswords)]
    print (z)
    for rows in z:          
        row_index = z.index(rows)
        single_row = ''.join(rows)
        print (single_row)
        column_index = single_row.find(word)
        print (column_index)
        if column_index >= 0:
            print([column_index, row_index])
        
    
    
    
crosswords=[['a','b','c','d'],['e','c','g','h'],['i','a','k','l'],['m','t','o','p']]
word='cat'
find_word_vertical (crosswords,word)
