# Type your code here
def calculate_gcd(a, b):
    if a == 0 or b == 0:
        return 0
    elif a == 1 or b == 1:
        return 1
    elif b % a == 0:
        return a
    elif a % b == 0:
        return b
    else:
        return calculate_gcd(a % b, b % a)
    
print (calculate_gcd (15,10))
    