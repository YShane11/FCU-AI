x=list(map(str,input().split()))
if x[9]=='X':
    x[9]=10
for i in range(9,-1,-1):
    a=0
    for j in range(0,i+1):
        a+=int(x[j])
    x[i]=a
for i in range(9,-1,-1):
    a=0
    for j in range(0,i+1):
        a+=int(x[j])
    x[i]=a
if x[9]%11==0:
    print('Yes')
else:
    print('No')
