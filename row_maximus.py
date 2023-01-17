def row_maximums(my_multidimensional_list):
    result = {}   
    for row in my_multidimensional_list:
        max_row = 0
        n = my_multidimensional_list.index (row)
        for i in row:
            if i >= max_row:
                max_row = i
                key_n = 'row '+str(n)+' max'
        result [key_n] = max_row
    print (result)
            

row_maximums ([[5, 0, 0, 0, 13],
 [0, 12, 0, 0],
 [20, 0, 11, 0],
  [6, 0, 0, 8]])