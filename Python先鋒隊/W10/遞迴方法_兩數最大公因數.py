def fun(n,m):
    if n%m == 0:
        return m
    else:
        return fun(m,n%m)
x,y=map(int,input().split())
print(fun(max(x,y),min(x,y)))