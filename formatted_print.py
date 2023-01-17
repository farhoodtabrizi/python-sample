def formatted_print(d):
    v_l = list(d.values())
    v_l.sort()
    for i in v_l[-1::-1]:
        for j in d:
            if d[j] == i:
                print (f'{j:<10s} {d[j]:>6.2f}')
        
    
    
    
formatted_print ({'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900})