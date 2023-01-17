def multiplication_table(n):
    main_res = []     
    for i in range (1,n+1):
        result = []
        for j in range (1,n+1):
            a = i*j
            result.append (a)
        main_res.append (result)
    print (main_res)

    
multiplication_table(4)
