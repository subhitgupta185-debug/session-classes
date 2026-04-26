import pandas as pd

df = pd.read_csv("sales_data.csv")


# Clear names reduce confusion
# Rename price to unit price

df = df.rename(columns={"Price": "Unit price", "Discount" : "Discount percent"})
print(df)

print("Hello")
# Drop

df_2 = df.drop(columns=["orderdate", "DiscountPercent"])
print(df_2)
