import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df)


# Average revenue per order :
df["Revenue"] = df["Quantity"] * df["Price"]
df_order = df.groupby("Region")["Revenue"].mean()
print(df_order)


# How many orders per region ? 

df_count = df.groupby("Region")["OrderID"].count()
print(df_count)


# What is the difference between count and size ?
print("Hello")
df_size = df.groupby("Region").size()
print(df_size)


# Show sum, mean and count together : 

df_agg = df.groupby("Region")["Revenue"].agg(["sum", "mean", "count"])
print(df_agg)


# Revenue only on sum and mean and count of OrderID :
df_split = df.groupby("Region").agg({
    "Revenue" : ["sum", "mean"],
    "OrderID" : "count"
})
