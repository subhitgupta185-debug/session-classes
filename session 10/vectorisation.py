numbers = [1,2,3,4]
#out = [2,4,6,8]


square = []
for i in numbers:
    square.append (i * 2)
    
print(square)


import numpy as np
numbers_np = np.array([1,2,3,4])
squared_np = numbers_np * 2

print(squared_np)



# multiply [10,20,30] by 5. 

numbers_np = np.array([10,20,30])
mul_np = numbers_np * 5
print(mul_np)

