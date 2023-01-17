def digit_words(sample_integer):
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"0" : ["zero", ""],
                         "1" : ["one", ""],
                         "2" : ["two","twenty"],
                         "3" : ["three","thirty"],
                         "4" : ["four","forty"],
                         "5" : ["five","fifty"],
                         "6" : ["six","sixty"],
                         "7" : ["seven","seventy"],
                         "8" : ["eight","eighty"],
                         "9" : ["nine","ninety"],
                         "10" : "ten",
                         "11" : "eleven",
                         "12" : "twelve",
                         "13" : "thirteen",
                         "14" : "fourteen",
                         "15" : "fifteen",
                         "16" : "sixteen",
                         "17" : "seventeen",
                         "18" : "eighteen",
                         "19" : "nineteen"}

    thousand_digit = sample_dictionary[splitted[0]][0]
    hundred_digit = sample_dictionary[splitted[1]][0]
    ten_digit = sample_dictionary[splitted[2]][0]
    one_digit = sample_dictionary[splitted[3]][0]

    my_list = []
    # Work with the thousand digit
    my_list.append(thousand_digit)
    my_list.append("thousand")

    if hundred_digit != "zero":
        my_list.append(hundred_digit)
        my_list.append("hundred")

    if ten_digit == "zero" and one_digit != "zero":
        my_list.append(one_digit)

    if ten_digit != "zero" and one_digit == "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)

    if ten_digit != "zero" and ten_digit != "one" and one_digit != "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)
        last_digit = sample_dictionary[splitted[3]][0]
        my_list.append(last_digit)

    if ten_digit != "zero" and ten_digit == "one" and one_digit != "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    if ten_digit != "zero" and ten_digit == "one" and one_digit == "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    # remove any "" that the list contains
    # due to the way the program was implemented
    if "" in my_list:
        my_list.remove("")
    out_string = ""
    out_string = ' '.join(my_list)
    return out_string