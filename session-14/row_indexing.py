import pandas as pd

# Now reading row indexing : 

df = pd.read_csv("employees.csv")
print(df.iloc[0 : 3])
print(df.loc[0:3])

print(df)

df.index = ["a", "b", "c", "d" , "e", "f", "g", "h", "i"]  # Labels
print(df.loc["a"])

# Use loc use labels otherwise use index 