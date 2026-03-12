# Q1: .loc[] vs .iloc[]

**.loc[]**: Label-based indexing - uses index labels (inclusive)
**.iloc[]**: Integer-based indexing - uses integer positions (exclusive end)

**Example with numeric index (0,1,2,3,4):**
```python
df.loc[0:3]  # Returns rows with labels 0,1,2,3 (4 rows)
df.iloc[0:3]  # Returns rows at positions 0,1,2 (3 rows)
```

**Example with string index ('a','b','c','d','e'):**
```python
df.loc['a':'c']  # Returns rows with labels 'a','b','c' (3 rows)
df.iloc[0:3]  # Returns rows at positions 0,1,2 (3 rows)
```

# Q2: analyze_csv() function

```python
import pandas as pd

def analyze_csv(filepath):
    df = pd.read_csv(filepath)
    
    print("=== First 5 Minutes Checklist ===")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print(f"Data types:\n{df.dtypes}")
    print(f"Missing values:\n{df.isnull().sum()}")
    print(f"First few rows:\n{df.head()}")
    
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    null_counts = df.isnull().sum().to_dict()
    memory_mb = df.memory_usage(deep=True).sum() / (1024 * 1024)
    
    return {
        'num_rows': len(df),
        'num_cols': len(df.columns),
        'numeric_cols': numeric_cols,
        'categorical_cols': categorical_cols,
        'null_counts': null_counts,
        'memory_mb': memory_mb
    }
```

# Q3: Bug fixes

**Bug 1:** Use `&` instead of `and` for pandas boolean operations
```python
high_earners = df[(df["age"] > 25) & (df["salary"] > 55000)]
```

**Bug 2:** Use `.loc[]` for assignment to avoid chained indexing
```python
df.loc[0, "age"] = 26
```

**Bug 3:** `.iloc[0:2]` correctly returns 2 rows (positions 0,1), not 3
```python
first_two = df.iloc[0:2]  # Correctly gets 2 rows
# For 3 rows, use: df.iloc[0:3]
```
