n=int(input())
x=list(map(int,input().split()))
x.sort()
def fun(i):
    a=x[i]//1000
    b=(x[i]-(x[i]//1000)*1000)//100
    c=(x[i]-(x[i]//100)*100)//10
    d=x[i]-(x[i]//10)*10
    return a+b+c+d

for i in range(n):
    for j in range(n):
        if fun(i)<fun(j):
            x[i],x[j]=x[j],x[i]
for i in x:
    print(i,end=' ')
