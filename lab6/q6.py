# Write a Pandas program to find out the alcohol consumption details in the year '1987' or
# '1989' from the world alcohol consumption dataset.

import pandas as pd


url = 'https://raw.githubusercontent.com/Srijaali/Python_PAI/refs/heads/main/lab6/q5_alcohol.csv'

alcohol = pd.read_csv(url)

alcohol = alcohol[(alcohol['Year'] == 1987 )| (alcohol['Year']==1989)]
print(alcohol)


print("Shape of the dataset:", alcohol.shape)


print("Column names:", alcohol.columns)
