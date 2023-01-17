def anagrams(my_string1, my_string2):
    s1=my_string1.lower()
    s2=my_string2.lower()
    l=list(s2)
    if len (s1) != len (s2):
        return False
    for i in s1:
        if i not in l:
            return False
        l.remove(i)
    return True

anagrams ("Orchestra", "Carthorse")
