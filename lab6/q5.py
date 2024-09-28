# Write a Pandas program to display the dimensions or shape of the World alcohol
# consumption dataset. Also extract the column names from the dataset.

import pandas as pd


url = 'https://raw.githubusercontent.com/Srijaali/Python_PAI/refs/heads/main/lab6/q5_alcohol.csv'

alcohol = pd.read_csv(url)

print(alcohol)


print("Shape of the dataset:", alcohol.shape)


print("Column names:", alcohol.columns)
