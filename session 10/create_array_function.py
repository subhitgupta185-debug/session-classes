#  from existing data

import numpy as np
np.array([1,2,3])


# create an empty numpy 0s..

empty_arr = np.zeros(5)
print(empty_arr)


# Print 1 in numpy array for 10 elements : 

one_arr = np.ones(10)
print(one_arr)

# Create evenly space values with gap of 2, under 10 :
arange_np = np.arange(0, 10, 2)
print(arange_np)



# evenly spaced values : 
# Linespace : lineraly spaced numbers --> it generates evenly spaced numbers between a start and end value.

linear_np = np.linspace(0, 1, 5)
print(linear_np) 
# means : 
# starts = 0
# ends = 1
# Total numbers = 5 
# Includes both0 and 1:

# Step = (stop - start)/ ( num - 1) = (1-0)/(5-1)= 0.25
#step  #Value
# 0      0
# 1     0.25
# 2     0.50
# 3     0.75
# 4     1