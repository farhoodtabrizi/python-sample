def capitalize_word_in_crossword (crossword,word):
    
    
    def find_word_horizontal(crossword,word):
        w_l = list (word)
        d = len (w_l)
        for i in crossword:  
            m = crossword.index(i)
            for k in i:
                 n = i.index(k)
                 if  w_l == i[n:(n+d)]:   
                     i[n:(n+d)] = [x.upper() for x in i[n:(n+d)]]
                     return (crossword)

    def find_word_vertical(crossword,word):
        w_l = list (word)
        d = len (w_l)
        soton = [list(i) for i in zip(*crossword)]
        for i in soton:          
            m = soton.index(i)
            for k in i:
                 n = i.index(k)
                 if  w_l == i[n:(n+d)]:   
                     i[n:(n+d)] = [X.upper() for X in i[n:(n+d)]]
                     crossword = [list(x) for x in zip(*soton)]
                     return (crossword)
                     
    if find_word_horizontal(crossword,word) != crosswords:
        print ('horizontal', crossword)
    elif find_word_vertical(crossword,word) != crosswords:
        print ('vertical', crossword)
    else:
        print ('None')
    
                 
                  
crosswords=[['a','b','c','d'],['e','c','a','b'],['i','a','t','l'],['m','t','o','p']]
word='cat'
capitalize_word_in_crossword (crosswords,word)

                    