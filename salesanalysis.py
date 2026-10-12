import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

print(df.head())

df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)

total_profit = df['Profit'].sum()
print("Total Profit:", total_profit)

top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop Products:\n", top_products)

plt.figure(figsize=(8,5))
top_products.plot(kind='bar')
plt.title("Top 5 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

daily_sales = df.groupby('Date')['Sales'].sum()

plt.figure(figsize=(10,5))
daily_sales.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x='Category', y='Sales', data=df, estimator=sum)
plt.title("Category-wise Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
