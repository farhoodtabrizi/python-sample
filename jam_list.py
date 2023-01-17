def sum_list (listam):
    jam = []
    m = len(listam[0])
    for nn in range (m):
        sum_k= 0
        for i in listam:
            sum_k += i[nn]
        jam.append(sum_k)
    #print (jam)
    return jam

sum_list ([[1,2,3,4],
           [5,6,7,8],
           [10,11,12,13]])