import pandas as pd

df = pd.read_csv("sales_data.csv")



# detect missing data

print(df.isnull())


# Count missing values per column :
print(df.isnull().sum()) 



# Avengers Ironman Hulk
# Avengers ""   ""   ---> remove?

df_clean = df.dropna()
print(df)
print(df_clean)

# Drop only rows where quantity is missing
print("Now :")
df_clean2 = df.dropna(subset=["Quantity","Price"])
print(df_clean2)



# Drop column with missing values

df_clean3 = df.dropna(axis=1)
print(df_clean3)
                               



# Strategy 2 : filling missing values
# instead of removing data, replace missing with logical value
# 
# Fill discount 0
df["Discount"] = df["Discount"].fillna(0)
print(df)


mean = df["Price"].mean()
df["Price"] = df["Price"].fillna(mean)
print(df)

median = df["Price"].median()
df["Price"] = df["Price"].fillna(median)
print(df)