import pandas as pd 
import matplotlib.pyplot as plt
data = {
    "days" : [1, 2, 3, 4, 5],
    "users" : [120, 150, 170, 160, 180],
    "purchases": [30, 35, 40, 38, 45]
}

df = pd.DataFrame(data)


plt.plot(df["days"], df["users"], linestyle="--", marker = "o", linewidth = 5, color="red", markerfacecolor="black", label="users") # It's O not zero...
plt.plot(df["days"], df["purchases"], linestyle="--", marker = "^", linewidth = 3, color="blue", markerfacecolor="black", label="purchases")
plt.grid(True)
plt.legend()

plt.text(3,170, "peak day", fontsize= 12, fontweight= 1, color="red")
plt.show()
# Limited markers supported here : X[Cross], S[Square], o[circle], ^ [Traingle]
