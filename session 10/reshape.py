import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshape = arr.reshape(2, 3)

print(reshape)


# Wrong one :
arr_2 = np.array([1, 2, 3, 4, 5])
reshape_2 = arr_2.reshape(2,3)
#print(reshape_2)
# Here 2 * 3 = 6 elemnts but array has only 5 elements, that's why error occured.....



print(len(arr))

total = np.sum(arr_2)
