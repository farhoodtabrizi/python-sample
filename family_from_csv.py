def family_from_csv (filename):
    result = {}
    my_file = open('family.csv', 'r')
    data = my_file.readlines()
    for line in data:
        if line[0] != "#":
            # Split the line with the delimiter comma (',')
            first_name, last_name, age = line.replace(' ','').split(',')
            if last_name not in result:
                result[last_name] = {first_name: int(age)}
            else:
                if first_name not in result[last_name]:
                    result[last_name][first_name] = int(age)

    print (result)

family_from_csv ('a')