import numpy as np

a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [1, 3]])
c = a * b
print(c)

# matrix
c = a @ b
print(c)

c = a.dot(b)
print(c)

a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))
a *= 3
print(a)

b += a
print(b)

c = a + b
d = np.exp(c * 1j)
print(d.dtype.name)

sum = np.random.random((3, 3))
print(sum.sum())
print(sum.min())
print(sum.max())
print(sum.cumsum(axis=1))
print(sum.min(axis=1))

print()
s = np.arange(12).reshape(3, 4)
print(s.sum(axis=0))
print(s)
print(s.min(axis=1))
print(s.cumsum(axis=1))
