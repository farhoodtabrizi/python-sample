def list2to1 (listam):
    nlist = []
    for i in listam:
        for k in i:
            nlist.append(k)
    nlist.sort()
    print (nlist)
    
list2to1 ([[1,2,3],[4,5,6],[10,11,11,22]])