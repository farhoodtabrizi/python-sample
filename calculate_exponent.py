# Type your code here
def calculate_exponent(a, b):
    if a == 0:
        return 0
    elif a == 1 or b == 0:
        return 1
    else:
        return a * calculate_exponent(a, b - 1)
    
    
print (calculate_exponent(5,3))

    