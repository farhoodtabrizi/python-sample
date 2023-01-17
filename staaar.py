def star(n):
    m=1
    while (m<=n):
        print(m*'*')
        m=m+1
    p=n-1
    while (p>=1):
        print(p*'*')
        p=p-1
n=int(input('enter a number bigger than 3:'))
star(n)
