def v_character_in_str (S):
    dict_s = {}
    s = S.lower().replace(' ','')
    for i in s:
        if i in ['a','e','i','o','u']:
            count = s.count (i)
            s.replace(i, '')
            dict_s[str(i)] = count
    print (dict_s)

v_character_in_str ('hi my name is Farhood with double o')
