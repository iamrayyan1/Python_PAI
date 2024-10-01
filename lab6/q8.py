# You work for a small e-commerce company that sells products online. You have two CSV
# files: one containing product information and another containing order data. Your goal is to
# load and analyze this data using Pandas to answer specific questions. (use csv format to
# create and load data).
# 1) Product Information (products.csv)
# Columns: ProductID, ProductName, Category, Price
# 2) Order Data (orders.csv)
# Columns: Order ID, ProductID, Quantity, Order Date (MM-DD-YYYY)
# Tasks to perform:
# a. Load both CSV files into separate Pandas DataFrames.
# b. Display the first 5 and last 10 rows of each DataFrame to get an overview of the
# data.
# c. Calculate and display the total revenue generated from all orders.
# d. Find the top 5 best-selling products and top 5 low selling products.
# e. Determine the most common product category among the top 5 best-selling
# products.
# f. Calculate and display the average price of products in each category.

# g. Find the day, month and year separately with the highest total revenue.
# h. Create a new DataFrame that shows the total revenue for each month.
# i. Check if the data has any null values or invalid characters,

import pandas as pd

order_csv = 'https://raw.githubusercontent.com/Srijaali/Python_PAI/refs/heads/main/lab6/q8_order.csv'
prod_csv = 'https://raw.githubusercontent.com/Srijaali/Python_PAI/refs/heads/main/lab6/q8_prod.csv'

order = pd.read_csv(order_csv)
prod = pd.read_csv(prod_csv)

#printing the top 5 rows
print("First 5 rows of Products and Orders..\n")
print(order.head(5))
print("\n")
print(prod.head(5))
print("\n")

#printing the last 10 rows
print("Last 10 rows of Products and Orders..\n")
print(order.tail(10))
print("\n")
print(prod.tail(10))

# getting the total revenue
merging = pd.merge(order,prod , on='ProductID')
merging['Revenue'] = merging['Price'] * merging['Quantity']
total_rev = merging['Revenue'].sum()
print("\nTotal Revenue of all products is: ", total_rev)

#top 5 best-selling
merging_df = pd.merge(order,prod , on='ProductID')
sales = merging_df.groupby(['ProductID' , 'ProductName'])['Quantity'].sum().reset_index()
best_worst = sales.sort_values(by='Quantity' , ascending = False)

best_selling = best_worst.head(5)
worst_selling = best_worst.tail(5)

print(f"\nThe top 5 best selling products are: {best_selling}")
print(f"\nThe top 5 worst selling products are: {worst_selling}")

#most common
merging_df = pd.merge(order,prod , on='ProductID')
sales = merging_df.groupby(['ProductID' , 'ProductName','Category'])['Quantity'].sum().reset_index()
best_worst = sales.sort_values(by='Quantity' , ascending = False)
best_selling = best_worst.head(5)
common = best_selling['Category'].mode()[0]
print(f"\nThe most common among best selling is: {common}")

#average price
average_price = prod.groupby(['Category'])['Price'].mean()
print(f"\nThe average price of all products is: {average_price}")

#day month year with highest total rev
merging['Order Date'] = pd.to_datetime(merging['Order Date'])  # Convert Order Date to datetime

merging['Day'] = merging['Order Date'].dt.day
merging['Month'] = merging['Order Date'].dt.month
merging['Year'] = merging['Order Date'].dt.year

day_revenue = merging.groupby('Day')['Revenue'].sum().reset_index()
month_revenue = merging.groupby('Month')['Revenue'].sum().reset_index()
year_revenue = merging.groupby('Year')['Revenue'].sum().reset_index()

best_day = day_revenue.loc[day_revenue['Revenue'].idxmax()]
best_month = month_revenue.loc[month_revenue['Revenue'].idxmax()]
best_year = year_revenue.loc[year_revenue['Revenue'].idxmax()]

print(f"\nThe day with the highest total revenue is: Day {best_day['Day']} with revenue {best_day['Revenue']}")
print(f"\nThe month with the highest total revenue is: Month {best_month['Month']} with revenue {best_month['Revenue']}")
print(f"\nThe year with the highest total revenue is: Year {best_year['Year']} with revenue {best_year['Revenue']}")

#new data frame to show total rev for each month
merging['Order Date'] = pd.to_datetime(merging['Order Date'])
merging['Month'] = merging['Order Date'].dt.month
month_revenue = merging.groupby('Month')['Revenue'].sum().reset_index()
month_revenue.columns = ['Month' , 'Total Rev']
print("\nTotal revenue for months:")
print(month_revenue)

#null or invalid characters
null_values = merging.isnull().sum()
print("\nNull values in each column:")
print(null_values)

invalid_quantity = merging[~merging['Quantity'].apply(lambda x: isinstance(x, int) and x >= 0)]
invalid_price = merging[~merging['Price'].apply(lambda x: isinstance(x, (int, float)) and x >= 0)]

# Print invalid entries if any
if not invalid_quantity.empty:
    print("\nInvalid Quantity Entries:")
    print(invalid_quantity)

if not invalid_price.empty:
    print("\nInvalid Price Entries:")
    print(invalid_price)

if invalid_quantity.empty and invalid_price.empty:
    print("\nNo invalid entries found in Quantity and Price.")
