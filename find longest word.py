def find_longest_word(input_string):
    l_s = input_string.split()
    print (l_s)
    len_l = 1
    for i in l_s:
        if len (i) >= len_l:
            len_l = len (i)
            n = l_s.index(i)
            print (len_l)
    print (l_s[n])
    return l_s [n]

find_longest_word ('hgsjhdf uyh knwejbfj dsfe') 
