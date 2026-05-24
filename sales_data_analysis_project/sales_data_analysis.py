# Author: Saloni Tiwari
# Topic: Sales Data Analysis (Pandas + Matplotlib)
# Description: Analyze and visualize sales data

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Display data
print("Dataset:\n", df)

# ---- Line Plot ----
plt.figure(figsize=(10, 6))

plt.plot(df['Month'], df['Product_A'], label='Product A', marker='o')
plt.plot(df['Month'], df['Product_B'], label='Product B', marker='s')
plt.plot(df['Month'], df['Product_C'], label='Product C', marker='^')

plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.savefig("line_plot_sales.png")
plt.show()

# ---- Bar Chart ----
df.set_index('Month').plot(kind='bar', figsize=(10, 6))

plt.title("Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.savefig("bar_chart_sales.png")
plt.show()

# ---- Pie Chart (May data) ----
may_data = df.iloc[-1, 1:]

plt.figure(figsize=(6, 6))
plt.pie(may_data, labels=may_data.index, autopct='%1.1f%%')

plt.title("Sales Distribution in May")

plt.savefig("pie_chart_sales.png")
plt.show()