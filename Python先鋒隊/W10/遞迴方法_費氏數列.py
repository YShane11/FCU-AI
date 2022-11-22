def fun(x):
    if x==0:
        return 0
    if x==1:
        return 1
    else:
        return fun(x-1)+fun(x-2)
x=int(input())
print(fun(x))