def _dictionary_names_grades_sample_(sample_dictionary):
    output_list = []
    keys = sample_dictionary.keys()
    for k in keys:
        each_list = sample_dictionary[k]
        grade1, grade2, grade3 = each_list[0], each_list[1], each_list[2]
        if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
            output_list.append(k)
    return output_list