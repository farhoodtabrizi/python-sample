def word_in_str (S):
    dict_s = {}
    s = S.lower()
    l = s.split()
    for word in l:
        counter = l.count (word)
        dict_s[word] = counter 
    print (dict_s)
    
word_in_str ('I am tall when I am young and I am short when I am old')
