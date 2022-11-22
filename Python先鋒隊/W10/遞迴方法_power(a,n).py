def power1(a,n):
    if n==1:
        return a
    else:
        return a*power1(a,n-1)
def power2(a,n):
    if n==1:
        return a
    elif a%2==0:
        return a*power2(a,n/2)*power2(a,n/2)
a,n=map(int,input().split())
print(power1(a,n))
if n%2==0:
    print(power2(a,n))
else:
    print(power1(a,n))