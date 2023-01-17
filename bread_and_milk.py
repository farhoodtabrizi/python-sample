def bread_and_milk (b):
    my_file = open('b_and_m.txt', 'r')
    data = my_file.readlines()
    res = {}
    milk_l = []
    bread_l = []
    for line in data:
        line = line.strip('\n').replace(' ','')
        if line [0] == 'm':
            t_line = list(line[1:])
            tl = []
            for i in t_line:
                i = float (i)
                tl.append(i)
            milk_l.append(tl)
        else:
            t_line = list(line[1:])
            tl = []
            for i in t_line:
                i = float (i)
                tl.append(i)
            bread_l.append(tl)
    res['milk'] = milk_l
    res['bread'] = bread_l
    print (res)
    my_file.close()
      
bread_and_milk ('a')

