import numpy as np

a = np.array([10, 20, 30, 40, 50])
# index        0   1   2  3   4

#[20, 30, 40]

print(a[1:4])



# 2D slicing:

matrix = np.array([
    [1,2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# [[2,3]]
#   [[5,6]]

# First two rows --> 0:2
# column 1 and 2 : 1:3


print(matrix[0:2, 1:3] )
print(matrix[1:3,0:2])



a = np.array([1, 2, 3, 4, 6, 8])
b = a[0:4]
print(b)
b[1] = 20
print(b)
print(a)

#Ques : Why did original change ?
# Ans 	:1)  Because slicing creates a view..
#	2) View means same memory
#	3)Just looking at the part of it
#	4) This behavious is intentional for performance but require awareness..



d = np.array([20,34,56,78,77])
e = d[0:5].copy()
print(e)
e[1] = 52
print(e)
print(d)