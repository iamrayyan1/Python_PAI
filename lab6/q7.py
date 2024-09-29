# Write a Pandas program to import excel data (employee.xlsx ) into a Pandas dataframe and
# find a list of employees of a specified year.

import pandas as pd

url = 'https://raw.githubusercontent.com/Srijaali/Python_PAI/main/lab6/q6_employee_data.xlsx'

df = pd.read_excel(url)

df_filtered = df[df["Year"] == 1993]
print(df_filtered)

