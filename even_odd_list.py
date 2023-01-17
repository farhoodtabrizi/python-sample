def sum_list (listam):
    even_l = []
    odd_l = []
    for i in listam:
        sum_k = 0
        for k in i:
            sum_k += k
        if sum_k % 2 == 0:
            even_l.append (sum_k)
        else:
            odd_l.append (sum_k)
    print ([len(even_l), len(odd_l)])
    
sum_list ([[1,2,3,4],[2,2,2],[3,3,3]])