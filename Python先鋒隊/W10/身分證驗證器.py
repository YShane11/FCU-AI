a = input()
x = [i for i in a]
X=ord(x[0])-55
X1=X//10
X2=X-(X//10)*10
P=int(X1)+9*int(X2)+8*int(x[1])+7*int(x[2])+6*int(x[3])+5*int(x[4])+4*int(x[5])+3*int(x[6])+2*int(x[7])+int(x[8])+int(x[9])
if P%10==0:
    print('CORRECT!!!')
else:
    print('WRONG!!!')