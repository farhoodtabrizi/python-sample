def calculate_grades (s):
    import numpy as farhood
    my_file = open('students.txt', 'r')
    data = my_file.readlines()
    my_file.close()
    result = []
    for line in data:
        res = []
        nomre = []
        line = list (line.replace(' ','').strip().split(','))
        for item in line[1:]:
            nomre.append(int(item))
            moadel = farhood.mean(nomre)
        res.append(line[0])
        res.append(moadel)
        result.append(tuple(res))
    print (tuple(result))
        

calculate_grades ('s')    