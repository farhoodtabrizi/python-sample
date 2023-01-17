def find_word_horizontal(crosswords,word):
    w_l = list (word)
    d = len (w_l)
    job = 'searching'
    for i in crosswords:  
        m = crosswords.index(i)
        if job != 'finish':
            for k in i:
                n = i.index(k)
                if  w_l == i[n:(n+d)]:
                    print ([m,n])
                    job = 'finish'
        elif job == 'searching':
             print ('farhood')

        
    
    
    
crosswords=[['v','c','y','t'],['c','n','t','m'],['a','c','n','t'],['c','u','t','k']]
word='cat'
find_word_horizontal(crosswords,word)