def create_grades_dict (s):
    import numpy as farhood
    my_file = open('scores.txt', 'r')
    data = my_file.readlines()
    my_file.close()
    result = {}
    tests = ['Test_1', 'Test_2', 'Test_3', 'Test_4']
    for line in data:
        res_v = []
        line = list (line.replace(' ','').strip().split(','))
        if len(line[1]) <= 15:
            res_v.append(line[1])
        if 'Test_1' in line [2:]:
            n = line.index('Test_1')
            if int (line[n+1]) >= 0 and int (line[n+1]) <= 100:
                res_v.insert(1,int (line[n+1]))
        else:
            res_v.insert(1,0)            
        if 'Test_2' in line [2:]:
            n = line.index('Test_2')
            if int (line[n+1]) >= 0 and int (line[n+1]) <= 100:
                res_v.insert(2,int (line[n+1]))
        else:
            res_v.insert(2,0)
        if 'Test_3' in line [2:]:
            n = line.index('Test_3')
            if int (line[n+1]) >= 0 and int (line[n+1]) <= 100:
                res_v.insert(3,int (line[n+1]))
        else:
            res_v.insert(3,0)
        if 'Test_4' in line [2:]:
            n = line.index('Test_4')
            if int (line[n+1]) >= 0 and int (line[n+1]) <= 100:
                res_v.insert(4,int (line[n+1]))
        else:
            res_v.insert(4,0)
        score = res_v [1:]
        moadel = farhood.mean(score)
        res_v.append(moadel)           
        result [line[0]] = res_v
    return result

def print_grades(s):
    grades_dict = create_grades_dict('s')
    header = ['ID', 'Name', 'Test_1', 'Test_2', 'Test_3', 'Test_4', 'Avg.']
    print ('{:^10s} | {:^16s} | {:^6s} | {:^6s} | {:^6s} | {:^6s} | {:^6s} |'.format(*header))
    for key, value in grades_dict.items():
        print (f"{key:<10s} | {value[0]:<16s} | {value[1]:>6d} | {value[2]:>6d} | {value[3]:>6d} | {value[4]:>6d} | {value[5]:>6.2f} |")

print_grades ('s')
