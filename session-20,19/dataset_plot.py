import pandas as pd 
import matplotlib.pyplot as plt
data = {
    "days" : [1, 2, 3, 4, 5],
    "users" : [120, 150, 170, 160, 180],
    "purchases": [30, 35, 40, 38, 45]
}

df = pd.DataFrame(data)

#print(df)


# Are users increasing over time ?

# day[x], # users[y]

#plt.plot(df["days"],df["users"])    # Just to mark x axis is for days and y axis is for number of users.
#plt.xlabel("Days")                  # Labeling X row
#plt.ylabel("Number of users")       # Labeling Y row
#plt.title("App users over time")    # Title input
#plt.show()                          # To show the output



# Are purchases increasing over time ?

plt.plot(df["days"],df["purchases"])
plt.xlabel("Number of days")
plt.ylabel("Number of purchases")
plt.title("Purchases per day")
plt.show()