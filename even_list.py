def even_list (listam):
    max_k = 0
    result = None
    if listam == []:
        return result
    for i in listam:
        for k in i:
            if k % 2 == 0:
                if k >= max_k:
                    max_k = k
                result = max_k
                return result        
            else:
                return result 