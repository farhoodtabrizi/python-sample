def sum_list (listam):
    jam = []
    m = len(listam[0])
    for nn in range (m):
        M = 0
        soton = []
        for i in listam:
            soton.append(i[nn])
            #print (soton)
            M=max(soton)
        #print (M)
        jam.append(M)
    #print (jam)
    return jam

sum_list ([[1,2,33,4],
           [5,16,7,81],
           [10,11,22,13]])
