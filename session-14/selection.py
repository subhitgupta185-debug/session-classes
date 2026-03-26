import pandas as pd

df = pd.read_csv("employees.csv")
print(df)

print("Marks : ")
x = df["marks"]
print(x)

print("Yo Yo double :")
y = df[["s.no", "marks", "department"]]
print(y)




