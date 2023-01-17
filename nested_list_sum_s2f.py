# Type your code here
def nested_list_sum(n):
    total = 0  # don't use `sum` as a variable name
    for i in n:
        if isinstance (i, list):  # checks if `i` is a list
            total += nested_list_sum(i)
        else:
            total += i
    return total

        
print(nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]]))