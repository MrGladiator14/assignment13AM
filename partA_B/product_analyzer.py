import pandas as pd
import numpy as np

data = {
    'name': [
        'Laptop Pro', 'Wireless Mouse', 'Python Cookbook', 'Cotton T-Shirt',
        'Smartphone X', 'Desk Lamp', 'Jeans', 'Headphones',
        'Data Science Handbook', 'Coffee Maker', 'Gaming Chair', 'Winter Jacket',
        'Tablet Plus', 'Blender', 'Wool Sweater', 'Bluetooth Speaker',
        'Machine Learning Guide', 'Air Purifier', 'Hoodie', 'Smart Watch',
        'Novel Collection', 'Microwave Oven', 'Running Shoes', 'Monitor Stand'
    ],
    'category': [
        'Electronics', 'Electronics', 'Books', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Home', 'Clothing',
        'Electronics', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Clothing', 'Electronics',
        'Books', 'Home', 'Clothing', 'Home'
    ],
    'price': [
        45000, 1500, 800, 600,
        35000, 2000, 2500, 3000,
        1200, 3500, 8000, 4500,
        25000, 4000, 1800, 5500,
        1500, 12000, 1500, 15000,
        900, 6500, 3200, 1500
    ],
    'stock': [
        45, 120, 80, 200,
        60, 35, 150, 90,
        65, 40, 25, 85,
        55, 30, 110, 75,
        95, 20, 180, 40,
        130, 45, 95, 60
    ],
    'rating': [
        4.5, 4.2, 4.8, 3.9,
        4.6, 4.1, 4.3, 4.7,
        4.9, 3.8, 4.4, 4.2,
        4.1, 3.7, 4.0, 4.5,
        4.6, 3.9, 3.8, 4.3,
        4.1, 3.6, 4.4, 4.0
    ],
    'num_reviews': [
        234, 156, 89, 312,
        445, 67, 198, 278,
        145, 78, 234, 167,
        389, 45, 223, 156,
        98, 34, 289, 412,
        76, 56, 145, 89
    ]
}

df = pd.DataFrame(data)

print("=== FIRST 5 MINUTES CHECKLIST ===")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Data types:\n{df.dtypes}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Basic statistics:\n{df.describe()}")
print(f"First 5 rows:\n{df.head()}")
print(f"Last 5 rows:\n{df.tail()}")

print("\n=== .LOC[] OPERATIONS ===")
electronics = df.loc[df['category'] == 'Electronics']
print(f"Electronics products ({len(electronics)} items):\n{electronics}")

high_rated_cheap = df.loc[(df['rating'] > 4.0) & (df['price'] < 5000)]
print(f"High rated (>4.0) and cheap (<5000) products ({len(high_rated_cheap)} items):\n{high_rated_cheap}")

df.loc[df['name'] == 'Laptop Pro', 'stock'] = 50
print(f"Updated stock for Laptop Pro: {df.loc[df['name'] == 'Laptop Pro', 'stock'].values[0]}")

print("\n=== .ILOC[] OPERATIONS ===")
first_five = df.iloc[:5]
print(f"First 5 products:\n{first_five}")

last_five = df.iloc[-5:]
print(f"Last 5 products:\n{last_five}")

every_other = df.iloc[::2]
print(f"Every other row ({len(every_other)} items):\n{every_other}")

subset = df.iloc[10:16, 0:4]
print(f"Rows 10-15, columns 0-3:\n{subset}")

print("\n=== FILTERED DATAFRAMES ===")
budget_products = df[df['price'] < 1000]
print(f"Budget products (<1000) ({len(budget_products)} items):\n{budget_products}")

premium_products = df[df['price'] > 10000]
print(f"Premium products (>10000) ({len(premium_products)} items):\n{premium_products}")

popular_products = df[(df['num_reviews'] > 100) & (df['rating'] > 4.0)]
print(f"Popular products (>100 reviews and >4.0 rating) ({len(popular_products)} items):\n{popular_products}")

print("\n=== EXPORTING TO CSV ===")
filtered_dfs = {
    'budget_products': budget_products,
    'premium_products': premium_products,
    'popular_products': popular_products
}

for name, dataframe in filtered_dfs.items():
    filename = f"{name}.csv"
    dataframe.to_csv(filename, index=False)
    print(f"Exported {len(dataframe)} items to {filename}")

print("\n=== ANALYSIS COMPLETE ===")
