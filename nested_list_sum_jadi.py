################### Sample Solution ###################
def nested_list_sum(sample_list):
    my_sum = 0
    for element in sample_list:
        if type(element) != type([]):
            my_sum += element
        else :
            my_sum += nested_list_sum(element)
    return my_sum