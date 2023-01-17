def spelling_corrector(s1,s2):
    s1=s1.lower().split()
    s2new=[i.lower() for i in s2]
    s3=[None]*(len(s1))
    for i in s1:
        if len(i)<=2:
            n=s1.index(i)
            s3[n]=s1[n]
        else:
            if i in s2new:
                n=s1.index(i)
                s3[n]=s1[n]
            for j in s2new:
                if len(i) - len(j) == -1:
                    if i == j[:-1] or i == j[1:]:
                        n=s1.index(i)
                        m=s2new.index(j)
                        s3[n]=s2new[m]
                    else:
                        for k in range(len(j)):
                            if i == j[:k] + j[k+1:]:
                                n=s1.index(i)
                                m=s2new.index(j)
                                s3[n]=s2new[m]
                elif len(i) - len(j) == 1:
                    if i[:-1] == j or i[1:] == j:
                        n=s1.index(i)
                        m=s2new.index(j)
                        s3[n]=s2new[m]
                    else:
                        for k in range(len(i)):
                            if j == i[:k] + i[k+1:]:
                                n=s1.index(i)
                                m=s2new.index(j)
                                s3[n]=s2new[m]

    print (s3)
    for i in s3:
        if i == None:
            n=s3.index(i)
            s3[n]=s1[n]
    result=''
    for i in s3:
        result=result+' '+i
    print (result)
    return result


spelling_corrector ('Thes is vary essy', ['this', 'is', 'very', 'very', 'easy'])
