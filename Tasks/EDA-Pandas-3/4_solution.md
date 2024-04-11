# Clues and Required API Information:

# 1. Pandas DataFrame Operations:
# - Use pd.read_csv() to read the CSV file into a DataFrame.
# - Use df.drop_duplicates() to remove duplicate rows.
# - Use df.dropna() to remove rows with missing values.
# - Use df.groupby() to group data by a specific column.
# - Use df.sum() to calculate the sum of values in a DataFrame or Series.

# 2. Numpy Array Operations:
# - Use np.array() to create a numpy array from a list or other sequence.
# - Use np.sum() to calculate the sum of array elements.

# 3. Additional Tips:
# - Remember to handle data types appropriately (e.g., converting strings to dates or numbers).
# - Pay attention to column names and use df.rename() if necessary.
# - Use descriptive variable names to improve code readability.
# - Break down the problem into smaller, manageable tasks and tackle them one by one.
# - Test your functions with sample data to ensure they work correctly.

# Feel free to refer to the Pandas and NumPy documentation for more information and examples:
# Pandas documentation: https://pandas.pydata.org/docs/
# NumPy documentation: https://numpy.org/doc/stable/

import pandas as pd
import numpy as np

def clean_data(file_path):
    """
    Function to clean up the given CSV file containing sales data.
    
    Args:
    file_path (str): Path to the CSV file.
    
    Returns:
    pd.DataFrame: Cleaned DataFrame with the following columns: 'date', 'product', 'quantity', 'price'.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Clean up data (remove duplicates, handle missing values, etc.)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    # Return the cleaned DataFrame
    return df

def calculate_total_sales(df):
    """
    Function to calculate total sales for each product.
    
    Args:
    df (pd.DataFrame): Cleaned DataFrame containing sales data.
    
    Returns:
    pd.DataFrame: DataFrame with total sales for each product.
    """
    # Convert 'quantity' and 'price' columns to numeric
    df['quantity'] = pd.to_numeric(df['quantity'])
    df['price'] = pd.to_numeric(df['price'])
    
    # Calculate total sales for each product
    df['total_sales'] = df['quantity'] * df['price']
    total_sales_df = df.groupby('product')['total_sales'].sum().reset_index()
    
    # Return DataFrame with total sales
    return total_sales_df

# Sample data
sample_data = """
date,product,quantity,price
2023-01-01,Apple,10,2.5
2023-01-02,Orange,20,1.8
2023-01-03,Banana,15,1.2
2023-01-04,Apple,12,2.8
2023-01-05,Orange,18,2.0
2023-01-06,Banana,10,1.5
"""

# Convert sample data string to DataFrame
from io import StringIO
sample_df = pd.read_csv(StringIO(sample_data))

# Clean the sample data
cleaned_sample_df = clean_data(StringIO(sample_data))

# Calculate total sales for each product
total_sales_df = calculate_total_sales(cleaned_sample_df)
print("Total Sales:")
print(total_sales_df)
