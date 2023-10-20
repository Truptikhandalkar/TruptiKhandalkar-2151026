import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data (you can load real data from a file or database)
sales_data = {
    'Date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
    'Product': ['Product1', 'Product2', 'Product1', 'Product2', 'Product1'],
    'Quantity': [10, 15, 8, 12, 7],
    'Revenue': [59.90, 164.85, 47.92, 131.88, 41.93]
}

# Create a DataFrame from the sales data
df = pd.DataFrame(sales_data)

# Convert the 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'])

# Analyze sales trends over time
daily_sales = df.groupby('Date')['Revenue'].sum()
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()

# Create data visualizations
plt.figure(figsize=(10, 5))

# Sales trends over time
plt.subplot(121)
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title('Daily Sales Trends')
plt.xlabel('Date')
plt.ylabel('Revenue')

# Popular products
product_sales = df.groupby('Product')['Quantity'].sum()
plt.subplot(122)
product_sales.plot(kind='bar')
plt.title('Popular Products')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')

# Identify peak sales hours (not from the provided data)
# You can add this information if available

# Generate reports
print("Monthly Sales Report:")
print(monthly_sales)

plt.tight_layout()
plt.show()
