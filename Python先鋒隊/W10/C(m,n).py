def fun(m,n):
    a=1
    b=1
    c=1
    for i in range(1,m+1):
        a*=i    
    for i in range(1,n+1):
        b*=i
    for i in range(1,m-n+1):
        c*=i
    return int(a/(b*c))
m,n=map(int,input().split())
print('{}'.format(fun(m,n)))


