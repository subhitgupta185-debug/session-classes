import pandas as pd


data = {
    "Name" : ["Alice", "Bob", "Charlie"],
    "Math" : [88, 92, 89],
    "science" : [88, 92, 89],
    "Computer" : [20, 522, 62]
}

df = pd.DataFrame(data)
print(df[["Math", "science", "Computer"]])


# Created index automatically
# understand data type automatically
# Formatted as table



details = {
    "name" : ["Alice", "Bob", "Charlie", "Dobby"],
    "Exp" : [5, 7, 8, 10],
    "salary" : [20000, 50000, 80000, 100000]
}

df = pd.DataFrame(details)

print(df[["name", "Exp", "salary"]])