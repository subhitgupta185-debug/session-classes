import pandas as pd

df = pd.read_csv("employees.csv")


c = df.sort_values("salary", ascending=False)
print(c)

z = df.sort_values(["salary", "marks"], ascending=[True, False])
print(z)
