def key_value (d):
    d_k = tuple(dict.keys(d))
    d_v = tuple(dict.values(d))
    result = (d_k , d_v)
    print (result)
    
key_value ({1:"a", 2:"b", 3:"c", 4:"d"})