def character_in_str (S):
    dict_s = {}
    s = S.lower().replace(' ','')
    for i in s:
        count = s.count (i)
        s.replace(i, '')
        dict_s[str(i)] = count
        
        
    print (dict_s)
    


character_in_str ('hi my name is Farhood with double o')