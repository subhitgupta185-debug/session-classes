import pandas as pd

arr = pd.Series([90, 85, 80])
print(arr)

arr_2 = pd.Series([90, 85, 80], index = ["Alice", "Bob", "Charlie"])
print(arr_2)
print(type(arr_2))


# Suppose you are analyzing
# Daily tempratures
# How will you create a pandas series for it ?

arr_3 = pd.Series(["Average temprature",20, 32, 10, 1], index = ["Days","Monday", "Tuesday", "Wednesday", "Thursday"])

print(arr_3)