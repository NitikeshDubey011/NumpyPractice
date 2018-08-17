import numpy as np


# Q. Convert the function maxx that works on two scalars, to work on two arrays.
# answer:
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


pair_max = np.vectorize(maxx, otypes=[float])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

# print(pair_max(a, b))

# Q. Swap columns 1 and 2 in the array arr.
# answer:
arr = np.arange(9).reshape(3, 3)
temp = np.copy(arr[:, 0])
arr[:, 0] = arr[:, 1]
arr[:, 1] = temp

# or

arr[:, [1, 0, 2]]

# Q: Reverse the rows of a 2D array arr.
# answer:
arr = np.arange(9).reshape(3, 3)
arr[::-1]

# Q. Reverse the columns of a 2D array arr.
# answer:
arr = np.arange(9).reshape(3, 3)
print(arr[:, ::-1])

# Q. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.
# answer:
arr = np.arange(9).reshape(3, 3)
rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr)

# Q. Print or show only 3 decimal places of the numpy array rand_arr.
# answer:
arr = np.random.random((5, 3))
np.set_printoptions(precision=3)
print(arr[:4])

# Q. Pretty print rand_arr by suppressing the scientific notation (like 1e10)
# answer:

np.set_printoptions(suppress=False)
arr = np.random.seed(100)
rand_arr = np.random.random([3, 3]) / 1e3
np.set_printoptions(suppress=True,precision=6)
print(rand_arr)