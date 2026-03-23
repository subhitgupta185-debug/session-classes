import pandas as pd

data = {
    "name" : ["Alice", "bob"],
    "age" : [25, 30],
    "salary" : [50000, 75000]
}


df = pd.DataFrame(data)
print(df)

# coloumns have name..
# Rows have index
# Easy filtering
