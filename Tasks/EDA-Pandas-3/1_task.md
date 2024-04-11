# Problem Statement:
- You are given a CSV file containing sales data in the following format:
- date,product,quantity,price
- The data is not well-formatted and contains inconsistencies and errors.
- Your task is to clean up the data using pandas and numpy, perform some operations,
- and output the result in a desired format.

# Your code should include the following functions:

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
    # Your code here
    
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
    # Calculate total sales for each product
    # Your code here
    
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

