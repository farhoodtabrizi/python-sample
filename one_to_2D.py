def one_to_2D(some_list, r, c):
    row = r
    column = c
    new_l = some_list
    main_res = []
    d = len(new_l) - r*c
    if d < 0:
        for k in range (abs(d)):
            new_l.append(None)
    for i in range (r):
        result = []
        for j in range (c):
            a = new_l[0]
            result.append (a)
            new_l.remove(a)
        main_res.append(result)
    print (main_res)
    
one_to_2D([8, 2, 9, 4], 2, 3)