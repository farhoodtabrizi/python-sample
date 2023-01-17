def dict_from_csv (b):
    my_file = open('test.csv', 'r')
    data = my_file.readlines()
    res = {}
    for i in data:
        i = i.strip('\n').split(',')
        i[1:] = list(map(float, i[1:]))
        res [i[0]] = i[1:]
    print (res)
    my_file.close()
       
dict_from_csv ('a')