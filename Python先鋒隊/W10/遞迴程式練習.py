import math
def fun(n):
    if n == 1:
        return n+1
    elif n > 1:
        return fun(n-1)+fun(math.floor(n/2))
n=int(input())
print(fun(n))