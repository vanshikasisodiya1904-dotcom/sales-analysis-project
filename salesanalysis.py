import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sales_data.csv")

# Show first rows
print(df.head())

# -------------------------
# DATA CLEANING
# -------------------------
df.dropna(inplace=True)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# -------------------------
# BASIC ANALYSIS
# -------------------------

# Total sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

# Total profit
total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

# Best selling products
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop Products:\n", top_products)

# -------------------------
# VISUALIZATION
# -------------------------

# 1. Top products bar chart
plt.figure(figsize=(8,5))
top_products.plot(kind='bar')
plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# 2. Sales trend over time
daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(10,5))
daily_sales.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# 3. Category-wise sales
plt.figure(figsize=(6,4))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title("Category-wise Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()