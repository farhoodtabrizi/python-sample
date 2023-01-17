def sum_list (listam):
    max_i = []
    for i in listam:
        max_a = 0
        for k in i:
            if k >= max_a:
                max_a = k
        max_i.append(max_a)
    print (max_i)

    
sum_list ([[1,2,5,3,4],[2,2,10,2],[3,4,3,3]])
