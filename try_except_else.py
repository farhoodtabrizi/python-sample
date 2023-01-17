def try_except_else ():
    try:
        a = input('Enter a number: \n')
        integer = int(a)
    except :
        print('Error')
    else:
        print(f"""the int() form your input is {integer}, and float is {float(integer)} and that's ok!""")
    finally :
        print(f'remeber: {a} is what you enter')
    print('down')
    
try_except_else()