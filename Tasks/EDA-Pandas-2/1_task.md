## Problem Statement: Analyzing Sales Data

You are given a dataset containing sales data for different products across multiple stores. Your task is to write Python functions and code fragments to perform the following tasks:

1. Calculate the total sales for each product across all stores.
2. Find the store with the highest total sales.
3. Calculate the average sales for each product.

The dataset is provided as a CSV file named `sales_data.csv`, with the following columns:
- `Product_ID`: ID of the product
- `Store_ID`: ID of the store
- `Sales`: Sales amount in dollars

You need to implement the following functions:

### 1. `total_sales_per_product(data: pd.DataFrame) -> pd.DataFrame`:
This function takes the sales data as input and returns a DataFrame containing the total sales for each product across all stores. The DataFrame should have two columns: `Product_ID` and `Total_Sales`.

### 2. `store_with_highest_sales(data: pd.DataFrame) -> int`:
This function takes the sales data as input and returns the ID of the store with the highest total sales.

### 3. Code Fragment:
Write a code fragment to calculate the average sales for each product and print the result.

```python
import pandas as pd

# Load the sales data
sales_data = pd.read_csv('sales_data.csv')

# Function to calculate total sales per product
def total_sales_per_product(data: pd.DataFrame) -> pd.DataFrame:
    total_sales = data.groupby('Product_ID')['Sales'].sum().reset_index()
    total_sales.columns = ['Product_ID', 'Total_Sales']
    return total_sales

# Function to find store with highest sales
def store_with_highest_sales(data: pd.DataFrame) -> int:
    store_sales = data.groupby('Store_ID')['Sales'].sum()
    return store_sales.idxmax()

# Code fragment to calculate average sales per product
average_sales = sales_data.groupby('Product_ID')['Sales'].mean()
print("Average Sales per Product:")
print(average_sales)


