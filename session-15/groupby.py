import pandas as pd

df = pd.read_csv("sales_data.csv")


df["Revenue"] = df["Quantity"] * df["Price"]
print(df)
#What is total revenue per region 

df_rev = df.groupby("Region")["Revenue"].sum()
print(df_rev)


# Which region earns most?
df_rev_sort = df_rev = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print(df_rev_sort)


# what is average revenue per region :
df_avg_rev = df_rev = df.groupby("Region")["Revenue"].sum().mean()
print(df_avg_rev)

