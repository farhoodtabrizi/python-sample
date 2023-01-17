character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
secret_key    = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"
def my_encryption(my_string):
    l1=list(character_set)
    l2=list(secret_key)
    l3=[]
    for i in my_string:
        m=l1.index(i)
        l3.append(l2[m])
    result=''.join(l3)
    print (result)
    return result

my_encryption ("Lets meet at the usual place at 9 am")