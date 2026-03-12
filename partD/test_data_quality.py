"""Test script for data quality report with various DataFrame scenarios."""

import pandas as pd
import numpy as np
from data_quality_report import generate_data_quality_report


def test_clean_dataframe():
    """Test with a clean, well-structured DataFrame."""
    print("=" * 80)
    print("TESTING WITH CLEAN DATAFRAME")
    print("=" * 80)
    
    clean_data = {
        'customer_id': range(1, 101),
        'name': [f'Customer_{i}' for i in range(1, 101)],
        'age': np.random.randint(18, 80, 100),
        'income': np.random.normal(50000, 15000, 100).round(2),
        'city': np.random.choice(['NYC', 'LA', 'Chicago', 'Houston'], 100),
        'active': np.random.choice([True, False], 100)
    }
    
    clean_df = pd.DataFrame(clean_data)
    report = generate_data_quality_report(clean_df)
    return report


def test_messy_dataframe():
    """Test with a messy DataFrame containing various data quality issues."""
    print("\n" + "=" * 80)
    print("TESTING WITH MESSY DATAFRAME")
    print("=" * 80)
    
    messy_data = {
        'id': [1, 2, 3, 4, 5, 5, 6, 7, 8, 9],  # Duplicate ID
        'name': ['Alice', 'Bob', None, 'Alice', 'Eve', 'Frank', '', 'Heidi', 'Ivan', 'Alice'],  # Missing and empty
        'age': [25, 30, 35, 25, 28, 32, None, 29, 31, 26],  # Missing value
        'salary': [50000, 60000, 70000, 50000, 55000, 65000, 72000, 58000, 68000, 52000],
        'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'IT', 'HR'],
        'useless_col': ['constant'] * 10,  # Single unique value
        'all_null_col': [None] * 10,  # All null column
        'mixed_types': ['text', 123, 'text', 456, 'text', 789, 'text', 101112, 'text', 131415],  # Mixed types
        'duplicates_row': ['A', 'B', 'C', 'A', 'B', 'C', 'D', 'E', 'F', 'G']  # Will create duplicate rows
    }
    
    # Create an exact duplicate row
    messy_data['id'].append(1)
    messy_data['name'].append('Alice')
    messy_data['age'].append(25)
    messy_data['salary'].append(50000)
    messy_data['department'].append('IT')
    messy_data['useless_col'].append('constant')
    messy_data['all_null_col'].append(None)
    messy_data['mixed_types'].append('text')
    messy_data['duplicates_row'].append('A')
    
    messy_df = pd.DataFrame(messy_data)
    report = generate_data_quality_report(messy_df)
    return report


def test_edge_cases():
    """Test edge cases like empty DataFrame and all-null columns."""
    print("\n" + "=" * 80)
    print("TESTING EDGE CASES")
    print("=" * 80)
    
    # Empty DataFrame
    print("Empty DataFrame:")
    empty_df = pd.DataFrame()
    empty_report = generate_data_quality_report(empty_df)
    
    # DataFrame with all null columns
    print("\nDataFrame with all-null columns:")
    all_null_data = {
        'col1': [None] * 5,
        'col2': [np.nan] * 5,
        'col3': [pd.NA] * 5
    }
    all_null_df = pd.DataFrame(all_null_data)
    all_null_report = generate_data_quality_report(all_null_df)
    
    # DataFrame with single unique value columns
    print("\nDataFrame with single unique value columns:")
    single_unique_data = {
        'constant_col': ['same_value'] * 10,
        'constant_num': [42] * 10,
        'normal_col': range(10)
    }
    single_unique_df = pd.DataFrame(single_unique_data)
    single_unique_report = generate_data_quality_report(single_unique_df)
    
    return empty_report, all_null_report, single_unique_report


if __name__ == "__main__":
    # Run all tests
    clean_report = test_clean_dataframe()
    messy_report = test_messy_dataframe()
    edge_case_reports = test_edge_cases()
    
    # Print summary for comparison
    print("\n" + "=" * 80)
    print("COMPARISON SUMMARY")
    print("=" * 80)
    print(f"Clean DataFrame - Missing values: {sum(clean_report['missing_values'].values())}")
    print(f"Messy DataFrame - Missing values: {sum(messy_report['missing_values'].values())}")
    print(f"Clean DataFrame - Duplicates: {clean_report['duplicates']}")
    print(f"Messy DataFrame - Duplicates: {messy_report['duplicates']}")
