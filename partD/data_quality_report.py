"""Data Quality Report Generator.

This module provides a comprehensive function to analyze and report on the quality
of pandas DataFrame objects, including shape, data types, missing values,
duplicates, uniqueness, and descriptive statistics.
"""

import pandas as pd
from typing import Dict, Any


def generate_data_quality_report(df: pd.DataFrame) -> Dict[str, Any]:
    """Generate a comprehensive data quality report for a pandas DataFrame.
    
    This function performs an automated audit of a DataFrame, calculating
    various quality metrics and returning them in a structured dictionary
    while also printing a formatted summary to the console.
    
    Args:
        df: pandas DataFrame to analyze
        
    Returns:
        Dictionary containing all calculated metrics with the following structure:
        {
            'shape': {'rows': int, 'columns': int},
            'data_types': Dict[str, str],
            'missing_values': Dict[str, float],
            'duplicates': int,
            'uniqueness': Dict[str, int],
            'descriptive_stats': Dict[str, Dict[str, float]]
        }
        
    Raises:
        TypeError: If input is not a pandas DataFrame
    """
    # Input validation
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    
    # Handle empty DataFrame edge case
    if df.empty:
        print("=" * 60)
        print("DATA QUALITY REPORT")
        print("=" * 60)
        print("⚠️  WARNING: Empty DataFrame provided")
        print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        print("=" * 60)
        
        return {
            'shape': {'rows': 0, 'columns': 0},
            'data_types': {},
            'missing_values': {},
            'duplicates': 0,
            'uniqueness': {},
            'descriptive_stats': {}
        }
    
    # Initialize report dictionary
    report = {}
    
    # 1. Shape analysis
    shape = df.shape
    report['shape'] = {'rows': shape[0], 'columns': shape[1]}
    
    # 2. Data types analysis
    data_types = df.dtypes.astype(str).to_dict()
    report['data_types'] = data_types
    
    # 3. Missing values analysis (percentage)
    missing_values = (df.isnull().sum() / len(df) * 100).round(2).to_dict()
    report['missing_values'] = missing_values
    
    # 4. Duplicates analysis
    duplicates = df.duplicated().sum()
    report['duplicates'] = duplicates
    
    # 5. Uniqueness analysis
    uniqueness = df.nunique().to_dict()
    report['uniqueness'] = uniqueness
    
    # 6. Descriptive statistics
    descriptive_stats = {}
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]) and not pd.api.types.is_bool_dtype(df[column]):
            descriptive_stats[column] = df[column].describe().round(4).to_dict()
        else:
            # For non-numeric or boolean columns, provide basic stats
            value_counts = df[column].value_counts()
            stats = {
                'count': df[column].count(),
                'unique': df[column].nunique(),
                'top': value_counts.index[0] if not value_counts.empty else None,
                'freq': value_counts.iloc[0] if not value_counts.empty else 0
            }
            descriptive_stats[column] = stats
    report['descriptive_stats'] = descriptive_stats
    
    # Print formatted console report
    _print_console_report(report)
    
    return report


def _print_console_report(report: Dict[str, Any]) -> None:
    """Print a formatted console summary of the data quality report.
    
    Args:
        report: Dictionary containing the data quality metrics
    """
    print("=" * 60)
    print("DATA QUALITY REPORT")
    print("=" * 60)
    
    # Shape section
    print("\n📊 SHAPE")
    print("-" * 30)
    shape = report['shape']
    print(f"Rows: {shape['rows']:,}")
    print(f"Columns: {shape['columns']:,}")
    
    # Data types section
    print("\n📋 DATA TYPES")
    print("-" * 30)
    for col, dtype in report['data_types'].items():
        print(f"{col}: {dtype}")
    
    # Missing values section
    print("\n❌ MISSING VALUES (%)")
    print("-" * 30)
    missing_report = report['missing_values']
    if missing_report:
        for col, percentage in missing_report.items():
            if percentage > 0:
                print(f"{col}: {percentage}%")
            else:
                print(f"{col}: 0%")
    else:
        print("No missing values found")
    
    # Duplicates section
    print("\n🔄 DUPLICATES")
    print("-" * 30)
    duplicates = report['duplicates']
    duplicate_percentage = (duplicates / report['shape']['rows'] * 100) if report['shape']['rows'] > 0 else 0
    print(f"Duplicate rows: {duplicates:,} ({duplicate_percentage:.2f}%)")
    
    # Uniqueness section
    print("\n🎯 UNIQUENESS")
    print("-" * 30)
    for col, unique_count in report['uniqueness'].items():
        total_rows = report['shape']['rows']
        uniqueness_percentage = (unique_count / total_rows * 100) if total_rows > 0 else 0
        print(f"{col}: {unique_count:,} unique values ({uniqueness_percentage:.1f}%)")
    
    # Descriptive statistics section
    print("\n📈 DESCRIPTIVE STATISTICS")
    print("-" * 30)
    for col, stats in report['descriptive_stats'].items():
        print(f"\n{col}:")
        for stat_name, stat_value in stats.items():
            if pd.notna(stat_value):
                # Format large numbers with commas
                if isinstance(stat_value, (int, float)) and stat_value > 1000:
                    print(f"  {stat_name}: {stat_value:,.4f}")
                else:
                    print(f"  {stat_name}: {stat_value}")
            else:
                print(f"  {stat_name}: N/A")
    
    print("\n" + "=" * 60)
    print("REPORT COMPLETE")
    print("=" * 60)


# Example usage and testing
if __name__ == "__main__":
    # Create sample data for testing
    sample_data = {
        'id': [1, 2, 3, 4, 5, 5, 6, 7, 8, 9],
        'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', None],
        'age': [25, 30, 35, 25, 28, 32, None, 29, 31, 26],
        'salary': [50000, 60000, 70000, 50000, 55000, 65000, 72000, 58000, 68000, 52000],
        'department': ['IT', 'HR', 'Finance', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'IT', 'HR']
    }
    
    # Create DataFrame and generate report
    test_df = pd.DataFrame(sample_data)
    print("Testing with sample DataFrame:")
    report = generate_data_quality_report(test_df)
    
    # Test with empty DataFrame
    print("\n\nTesting with empty DataFrame:")
    empty_df = pd.DataFrame()
    empty_report = generate_data_quality_report(empty_df)
