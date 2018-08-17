import numpy as np

# one dimensional arrays
a = np.arange(10) ** 3
print(a)
print(a[3])
print(a[2:5])

print()

for i in a:
    print(i ** (1 / 3.))

# two dimensional arrays

def f(x,y):
    return 10*x+y

b=np.fromfunction(f,(5,4),dtype=int)
print(b)

print(b[2,3])

print(b[0:5,0])

print(b[:,1])

print(b[1:3,:])

f = np.array(['Bonjour', 'Hello', 'Hallo',])
print(f.dtype)