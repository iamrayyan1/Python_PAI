# Write a python program using Pandas to get those movies whose revenue is more than 2
# million and spent less than 1 million.

import pandas as pd


data = {
    'title': ['Harry Potter', 'Cinderella', 'Inside Out', 'Interstellar' , 'Jab we Met'],
    'revenue': [2.5e6, 1.5e6, 3.0e6, 0.8e6 , 5.5e6],  # Revenue in millions
    'budget': [0.5e6, 0.9e6, 0.7e6, 1.0e6, 0.5e6]   # Budget in millions
}


df = pd.DataFrame(data)

filtered_movies = df[(df['revenue'] > 2e6) & (df['budget'] < 1e6)]

print(filtered_movies)
