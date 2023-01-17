def calculate_expenses(filename):
    my_file = open('expenses.txt', 'r')
    data = my_file.readlines()
    my_file.close()
    milk_s = 0
    bread_s = 0
    chips_s = 0
    for line in data:
        line = line.replace(' ','').strip().split(',')
        #print (line)
        if line[0] == 'milk':
            milk_s += float(line[1])
        elif line[0] == 'bread':
            bread_s += float(line[1])
        else:
            chips_s += float(line[1])
    milk_ss = '${:.2f}'.format(milk_s)
    bread_ss = '${:.2f}'.format(bread_s)
    chips_ss = '${:.2f}'.format(chips_s)
    result = []
    result.append(tuple(['bread', bread_ss]))
    result.append(tuple(['chips', chips_ss]))
    result.append(tuple(['milk', milk_ss]))
    print (result)
    
calculate_expenses('f')