def zarbM (a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list=[]
    temp_row=len(b[0])*[0]
    #print (temp_row)
    for r in range(len(a)):
        output_list.append(temp_row[:])
        #print (output_list)
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum=0
            for k in range(len(a[0])):
                sum=sum+a[row_index][k]*b[k][col_index]
            output_list[row_index][col_index]=sum
    return output_list
   


zarbM ([[1, 2, 3],[4, 5, 6]],[[11, 22, 33],[44, 55, 66],[77, 88, 99]])