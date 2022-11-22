import numpy as np
a=np.random.randint(0,10,(3,3))
b=np.random.randint(0,10,(3,3))


print(f'矩陣A為\n{a}')
print(f'矩陣B為\n{b}')
print(f'矩陣A+B為\n{a+b}')
print(f'矩陣A-B為\n{a-b}')
print(f'矩陣A*B為\n{a*b}')
print(f'A的轉至矩陣為\n{a.T}')