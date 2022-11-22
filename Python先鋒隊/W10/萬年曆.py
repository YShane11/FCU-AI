y,m=map(int,input().split())


print('SU','MO','TU','WE','TH','FR','SA',sep='\t')


w=0
for i in range(1,y+1):
    if (i%4==0) and (i%100 !=0) or (i%400)==0:
        w+=2
    else:
        w+=1
w=w%7
if m==1:
    w1=7-w
    d=31
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==2:
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        d=29
    else:
        d=28
    w=(w+31)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==3:
    d=31
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+60)%7
    else:
        w=(w+59)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==4:
    d=30
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+91)%7
    else:
        w=(w+90)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==5:
    d=31
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+121)%7
    else:
        w=(w+120)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==6:
    d=30
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+152)%7
    else:
        w=(w+151)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==7:
    d=31
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+182)%7
    else:
        w=(w+181)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==8:
    d=31
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+213)%7
    else:
        w=(w+212)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==9:
    d=30
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+244)%7
    else:
        w=(w+243)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==10:
    d=31
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+274)%7
    else:
        w=(w+273)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==11:
    d=30
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+305)%7
    else:
        w=(w+304)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')
elif m==12:
    d=31
    if (y%4==0) and (y%100 !=0) or (y%400)==0:
        w=(w+335)%7
    else:
        w=(w+334)%7
    w1=7-w
    print('  	'*w,end='')
    for i in range(1,w1):
        print(i,end='\t') 
    for i in range(w1,d+1):
        if (i-w1)%7==0:
            print(i)
        else:
            print(i,end='\t')