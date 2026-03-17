import numpy as np

a = np.array([10, 20, 30])
print(a.shape)


# meaning:
# 3 numbers in a straight line.

# Real life examples:
# 3 exam scores
# 3 tempratures
# 3 prices 



# 2D array also known as matrix

b = np.array([

    [1,2,3],
    [5,6,7]
    ])

print(b.shape)

# 2 rows and 3 coloums
# Real life examples
# excel sheet
# studen table
# datasets(rows and coloums)





# Three or more dimensions 
# now numpy supports arbitratily and dimensions


c = np.zeros((2, 3, 3, 4))
print(c.shape)
print(c)

# meaning
# There are 10 items
# each item has 3 values
# each Values as 3 rows
# each row has 4 coloums


# What does np.zero()
# created an array
# with shape (2,3)
# Fill it with 0


# why use it?
# When we want to create empty data

# If there are 5 students and 3 subjects
print('Hello')
print(np.zeros((5,3)))

# What does np.ones() mean?

print(np.ones((5, 3)))
# Or
z = np.ones((5, 3))
print(z)

# what is a Shape ?

# Shape tells 
# How many rows
# How many columns
# How many layers

# arr_name[row][col]

z[0][1] = 12
print(z)