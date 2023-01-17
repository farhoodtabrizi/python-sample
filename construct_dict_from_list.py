def construct_dictionary_from_lists(names, ages, scores):
    result = {}
    group = [list(i) for i in zip(names,ages,scores)]
    for row in group:
        if int(row[2]) >= 60:
            row.append('pass')
        else:
            row.append('fail')
        result[row[0]] = row[1:]
    print (result)
        
    
construct_dictionary_from_lists (["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60])