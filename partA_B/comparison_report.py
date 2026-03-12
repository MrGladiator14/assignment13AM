import pandas as pd
import numpy as np

january_data = {
    'product_id': range(1, 21),
    'product_name': [
        'Laptop Pro', 'Wireless Mouse', 'Python Cookbook', 'Cotton T-Shirt',
        'Smartphone X', 'Desk Lamp', 'Jeans', 'Headphones',
        'Data Science Handbook', 'Coffee Maker', 'Gaming Chair', 'Winter Jacket',
        'Tablet Plus', 'Blender', 'Wool Sweater', 'Bluetooth Speaker',
        'Machine Learning Guide', 'Air Purifier', 'Hoodie', 'Smart Watch'
    ],
    'units_sold': [45, 120, 80, 200, 60, 35, 150, 90, 65, 40, 25, 85, 55, 30, 110, 75, 95, 20, 180, 40],
    'unit_price': [45000, 1500, 800, 600, 35000, 2000, 2500, 3000, 1200, 3500, 8000, 4500, 25000, 4000, 1800, 5500, 1500, 12000, 1500, 15000],
    'category': [
        'Electronics', 'Electronics', 'Books', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Home', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Clothing', 'Electronics'
    ]
}

february_data = {
    'product_id': range(1, 21),
    'product_name': [
        'Laptop Pro', 'Wireless Mouse', 'Python Cookbook', 'Cotton T-Shirt',
        'Smartphone X', 'Desk Lamp', 'Jeans', 'Headphones',
        'Data Science Handbook', 'Coffee Maker', 'Gaming Chair', 'Winter Jacket',
        'Tablet Plus', 'Blender', 'Wool Sweater', 'Bluetooth Speaker',
        'Machine Learning Guide', 'Air Purifier', 'Hoodie', 'Smart Watch'
    ],
    'units_sold': [55, 95, 90, 180, 75, 45, 165, 85, 70, 50, 30, 95, 65, 35, 95, 80, 105, 25, 160, 50],
    'unit_price': [45000, 1500, 800, 600, 35000, 2000, 2500, 3000, 1200, 3500, 8000, 4500, 25000, 4000, 1800, 5500, 1500, 12000, 1500, 15000],
    'category': [
        'Electronics', 'Electronics', 'Books', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Home', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Clothing', 'Electronics'
    ]
}

march_data = {
    'product_id': range(1, 21),
    'product_name': [
        'Laptop Pro', 'Wireless Mouse', 'Python Cookbook', 'Cotton T-Shirt',
        'Smartphone X', 'Desk Lamp', 'Jeans', 'Headphones',
        'Data Science Handbook', 'Coffee Maker', 'Gaming Chair', 'Winter Jacket',
        'Tablet Plus', 'Blender', 'Wool Sweater', 'Bluetooth Speaker',
        'Machine Learning Guide', 'Air Purifier', 'Hoodie', 'Smart Watch'
    ],
    'units_sold': [50, 110, 85, 190, 70, 40, 155, 95, 75, 45, 28, 90, 60, 32, 100, 85, 100, 22, 170, 45],
    'unit_price': [44000, 1450, 750, 580, 34000, 1900, 2400, 2900, 1150, 3400, 7800, 4300, 24000, 3800, 1700, 5300, 1400, 11500, 1400, 14500],
    'category': [
        'Electronics', 'Electronics', 'Books', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Home', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Clothing', 'Electronics'
    ]
}

january_df = pd.DataFrame(january_data)
february_df = pd.DataFrame(february_data)
march_df = pd.DataFrame(march_data)

january_df['revenue'] = january_df['units_sold'] * january_df['unit_price']
february_df['revenue'] = february_df['units_sold'] * february_df['unit_price']
march_df['revenue'] = march_df['units_sold'] * march_df['unit_price']

print("=== MONTHLY SALES DATA ===")
print(f"January: {len(january_df)} products")
print(f"February: {len(february_df)} products")
print(f"March: {len(march_df)} products")

print("\n=== JANUARY METRICS ===")
jan_total_revenue = january_df['revenue'].sum()
jan_avg_order = january_df['revenue'].mean()
jan_top_product = january_df.loc[january_df['revenue'].idxmax(), 'product_name']
print(f"Total Revenue: ${jan_total_revenue:,.2f}")
print(f"Average Order Value: ${jan_avg_order:,.2f}")
print(f"Top-Selling Product: {jan_top_product}")

print("\n=== FEBRUARY METRICS ===")
feb_total_revenue = february_df['revenue'].sum()
feb_avg_order = february_df['revenue'].mean()
feb_top_product = february_df.loc[february_df['revenue'].idxmax(), 'product_name']
print(f"Total Revenue: ${feb_total_revenue:,.2f}")
print(f"Average Order Value: ${feb_avg_order:,.2f}")
print(f"Top-Selling Product: {feb_top_product}")

print("\n=== MARCH METRICS ===")
mar_total_revenue = march_df['revenue'].sum()
mar_avg_order = march_df['revenue'].mean()
mar_top_product = march_df.loc[march_df['revenue'].idxmax(), 'product_name']
print(f"Total Revenue: ${mar_total_revenue:,.2f}")
print(f"Average Order Value: ${mar_avg_order:,.2f}")
print(f"Top-Selling Product: {mar_top_product}")

summary_data = {
    'Total Revenue': [jan_total_revenue, feb_total_revenue, mar_total_revenue],
    'Average Order Value': [jan_avg_order, feb_avg_order, mar_avg_order],
    'Top Product': [jan_top_product, feb_top_product, mar_top_product]
}

summary_df = pd.DataFrame(summary_data, index=['January', 'February', 'March'])
print("\n=== SUMMARY COMPARISON ===")
print(summary_df)

print("\n=== USING .QUERY() METHOD ===")
high_revenue_jan = january_df.query("revenue > 100000")
print(f"January products with revenue > $100,000 ({len(high_revenue_jan)} items):")
print(high_revenue_jan[['product_name', 'revenue']])

electronics_feb = february_df.query("category == 'Electronics' and units_sold > 50")
print(f"\nFebruary Electronics with >50 units sold ({len(electronics_feb)} items):")
print(electronics_feb[['product_name', 'units_sold', 'revenue']])

low_performance_mar = march_df.query("units_sold < 40 or revenue < 50000")
print(f"\nMarch low performance products ({len(low_performance_mar)} items):")
print(low_performance_mar[['product_name', 'units_sold', 'revenue']])

print("\n=== FINDING OUTLIERS ===")

all_months_data = []
for df, month in [(january_df, 'January'), (february_df, 'February'), (march_df, 'March')]:
    df_copy = df.copy()
    df_copy['month'] = month
    all_months_data.append(df_copy)

combined_df = pd.concat(all_months_data, ignore_index=True)

top_5_revenue = combined_df.nlargest(5, 'revenue')
print("Top 5 Revenue Products (All Months):")
print(top_5_revenue[['month', 'product_name', 'revenue']])

bottom_5_revenue = combined_df.nsmallest(5, 'revenue')
print("\nBottom 5 Revenue Products (All Months):")
print(bottom_5_revenue[['month', 'product_name', 'revenue']])

top_3_units = combined_df.nlargest(3, 'units_sold')
print("\nTop 3 Units Sold Products (All Months):")
print(top_3_units[['month', 'product_name', 'units_sold']])

bottom_3_units = combined_df.nsmallest(3, 'units_sold')
print("\nBottom 3 Units Sold Products (All Months):")
print(bottom_3_units[['month', 'product_name', 'units_sold']])

print("\n=== ANALYSIS COMPLETE ===")
