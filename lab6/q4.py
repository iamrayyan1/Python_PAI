# Write a Pandas program to start index with different value rather than 0 in a given
# DataFrame.

import pandas as pd
import numpy as np

exam_data = {
    'Name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'Score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'Attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'Qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }

new_index = list(range(1,len(exam_data['Name'])+1))

df = pd.DataFrame(exam_data, index = new_index)
print(df)


