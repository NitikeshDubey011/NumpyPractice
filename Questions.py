# Q. Import numpy as `np` and print the version number.
# answer:
import numpy as np

print(np.__version__)

# Q: Create a 1D array of numbers from 0 to 9
# answer:
one_d = np.arange(0, 10)
print(one_d)

# Q. Create a 3×3 numpy array of all True’s
# answer:
three_dim = np.full((3, 3), True, dtype=bool)
print(three_dim)

# or
three_dim = np.ones((3, 3), dtype=bool)
print(three_dim)

# Q: Extract all odd numbers from arr
# answer:

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr % 2 == 1])

# Q: Replace all odd numbers in arr with -1
# answer:

arr[arr % 2 == 1] = -1
print(arr)

# Q: Replace all odd numbers in arr with -1 without changing arr
# answer:
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)

# Q:  Convert a 1D array to a 2D array with 2 rows
# answer:
arr = np.arange(10)
print(arr.reshape(2, 5))
# or
print(arr.reshape(2, -1))

# Q. Stack arrays a and b vertically
# answer:

a = np.arange(10).reshape(2, -1)
b = np.arange(10).reshape(2, -1)
print(np.vstack([a, b]))
# or
print(np.concatenate((a, b), axis=0))
# or
print(np.r_[a, b])

# Q. Stack the arrays a and b horizontally.
# answer:

a = np.arange(10).reshape(2, -1)
b = np.arange(10).reshape(2, -1)
print(np.hstack([a, b]))
# or
print(np.concatenate((a, b), axis=1))
# or
print(np.c_[a, b])

# Q: Create the following pattern without hard coding. Use only numpy functions and the below input array a.
# answer:

a = np.array([1, 2, 3])
b = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(b)

# Q: Get the common items between a and b
# answer:
a = np.array([1, 2, 3, 7, 5, 7, 7, 8, 9])
b = np.array([2, 2, 5, 4, 8, 9, 1, 1, 2])

print(np.intersect1d(a, b))

# Q: From array a remove all items present in array b
# answer:

a = np.array([1, 2, 3, 7, 5, 7, 7, 8, 9])
b = np.array([2, 2, 5, 4, 8, 9, 1, 1, 2])
print(np.setdiff1d(a, b))

# Q: Get the positions where elements of a and b match
# answer
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.where(a == b))

# Q. Get all items between 5 and 10 from a.
# answer:
a = np.array([2, 6, 1, 9, 10, 3, 27])
print(a[(a >= 5) & (a <= 10)])

