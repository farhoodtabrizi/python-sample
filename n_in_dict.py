def n_in_Dict (D, n):
    result = []
    keys = D.keys()
    for k in keys:
        each_values = D [k]
        if n in each_values:
            result.append(k)
    return result
            
        
    
    