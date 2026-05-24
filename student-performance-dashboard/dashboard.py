# =========================================================
# Author      : Saloni Tiwari
# Topic       : Student Performance Dashboard
# Description : Student marks analysis using Pandas
# =========================================================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD CSV FILE
# =========================

df = pd.read_csv("students.csv")

# =========================
# DISPLAY DATA
# =========================

print("\nStudent Data:")
print(df)

# =========================
# CALCULATE AVERAGE
# =========================

df["Average"] = (
    df["Math"] +
    df["Science"] +
    df["English"]
) / 3

print("\nAverage Marks:")
print(df[["Name", "Average"]])

# =========================
# FIND TOPPER
# =========================

topper = df.loc[df["Average"].idxmax()]

print("\nTopper:")
print(topper)

# =========================
# BAR CHART
# =========================

plt.figure(figsize=(8,5))

plt.bar(df["Name"], df["Average"])

plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")

plt.grid(True)

plt.savefig("charts/student_average_marks.png")

plt.show()

# =========================
# PIE CHART
# =========================

plt.figure(figsize=(6,6))

plt.pie(
    df["Average"],
    labels=df["Name"],
    autopct="%1.1f%%"
)

plt.title("Student Marks Distribution")

plt.savefig("charts/marks_distribution.png")

plt.show()

# =========================
# PROJECT COMPLETED
# =========================

print("\nDashboard Analysis Completed Successfully")