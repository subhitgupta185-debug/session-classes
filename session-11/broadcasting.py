import numpy as np

a = np.array([1, 2, 3])

print(a + 10)



# Why ?
# Numpy treat 10 like:
# [10, 10 ,10]
# And adds 

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([[10, 20, 30], [20, 36, 25]])

print(matrix + vector)

print(matrix.shape)
print(vector.shape)



mat = np.array([[10, 20],[25, 15]])
vec = np.array([20, 15])
print(vec + mat)