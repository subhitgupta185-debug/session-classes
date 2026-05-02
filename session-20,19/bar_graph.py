import matplotlib.pyplot as plt

models = ["Model A", "Model B", "Model C"]
sales = [40,55,48]

plt.bar(models, sales)

plt.xlabel("model")
plt.ylabel("Sales")
plt.title("No of sales per model")

plt.show()