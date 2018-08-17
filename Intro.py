import numpy as np
a=np.arange(15).reshape(3,5)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))
b=np.array([1.2,1.3,1.4])
print(b.dtype)
c=np.array([(1.5,2,3),(4,5,6)])
print(c)
# it will create array of zeroes
d=np.zeros((3,4))
print(d)
# it will create the array of ones
print(np.ones((3,3,4),dtype=np.int16))
# where first element is number of times it will print the array
# and second is row and third element is column.


# it will create the empty array with random values in it
print(np.empty((3,3)))
print()

# where 10 is the start and 35 is the end and last digit is range/difference
print(np.arange(10,35,3))
# another example
print(np.arange(0,2,0.3))



