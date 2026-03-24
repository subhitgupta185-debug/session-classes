import pandas as pd

df = pd.read_csv("abc.csv")
print(df)



# That single line :
# opens the file
# parese rows and columns
# data type infer
# constructed a dataframe

val = df.head(10)
print(val)

vel = df.tail()
print(vel)

val_3 = df.iloc[2 :7]
print(val_3)



info = df.info()
print(df.info)