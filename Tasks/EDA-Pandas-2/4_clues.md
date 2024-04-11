## Clues and API Information:

### Clue 1: Utilizing Pandas GroupBy
Pandas' `groupby()` function is extremely useful for performing operations on grouped data. It allows you to split data into groups based on some criteria and then apply a function to each group independently.

### Clue 2: Summing Values in a Group
To calculate the total sales for each product across all stores, you can use the `sum()` function after grouping by the 'Product_ID' column.

### Clue 3: Finding the Maximum Value in a Series
To find the store with the highest total sales, you can use the `idxmax()` function after grouping by the 'Store_ID' column and summing the sales.

### Clue 4: Calculating the Mean
To calculate the average sales for each product, you can use the `mean()` function after grouping by the 'Product_ID' column.

### Required Pandas API Information:
1. `groupby()`: Groups DataFrame using a mapper or by a Series of columns.
2. `sum()`: Returns the sum of the values for the requested axis.
3. `idxmax()`: Returns the index of the first occurrence of the maximum value.
4. `mean()`: Returns the mean of the values for the requested axis.

```python
# Code Fragment to Calculate Average Sales per Product
average_sales = sales_data.groupby('Product_ID')['Sales'].mean()
print("Average Sales per Product:")
print(average_sales)
