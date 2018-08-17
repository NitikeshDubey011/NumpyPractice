import numpy
import time
import sys

a = numpy.array([[2, 3, 4], [1, 2, 3], [7, 8, 9]])
print(a)
for row in a.flat:
    print(row)

b = numpy.arange(9).reshape(3, 3)
print(b)
a = numpy.vstack((a, b))
print(a)
b=numpy.hsplit(a,3)
print(b[0].ravel())
print(b[1].ravel())
print(b[2].ravel())


a=numpy.arange(12).reshape(3,4)
print(a)
for cell in a.flatten():
    print(cell)


for x in numpy.nditer(a,order='F',flags=['external_loop']):
    print(x)

for x in numpy.nditer(a,op_flags=['readwrite']):
    x[...]=x*x
print(a)


b=numpy.arange(3,15,4).reshape(3,1)
print(b)

for x,y in numpy.nditer([a,b]):
    print(x,y)