import pandas as pd


df = pd.read_csv("employees.csv")
print(df)

#print(df["salary"])
#print("Now filtered : ")

#x = df[df["salary"] > 100000] # Filtering dataframe df[], df["salary"] > 100000
#print(x)

#y = df[df["department"] == "AI"]
#print(y)


#z = df[(df["department"] == "AI") & (df["salary"] > 80000 )]   # Based on the sir's data
#print(z)


# Based on sir's data below

# Give me all employees whose department is AI or backend  |
#  df -----> Complete data


# a = df[# filter out department which is AI or Backend]
# a = df[(Condition 1) | (condition 2)]

# condition1 = df["department"] == "AI"
# condition 2 = df["department"] == "backend"

c = df[(df["department"] == "AI") | (df["department"] == "backend" )]
print(c)


# a = df["not department" = "frontend"]


#f = df[~(df["department"]) == ("frontend")]
#print(f)

            #OR

#f = df[(df["department"]) != ("frontend")]
#print(f)

