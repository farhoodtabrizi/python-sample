def dict_condition_from_csv (b):
    my_file = open('scores.csv', 'r')
    data = my_file.readlines()
    res = {}
    for line in data:
        if line [0] == '#':
            continue
        else:
            line = line.strip('\n').split(',')
            line[1:] = list(map(float, line[1:]))
            if line[1] and line[3] > 70:
                res [line[0]] = line[1:]
    print (res)
    my_file.close()
      
dict_from_csv ('a')
