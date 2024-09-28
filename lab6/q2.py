# Write a Pandas program to sort movies on runtime in descending order.

import pandas as pd

data = {
    'movies' : ["Harry Potter" , "Inception" , "Fast and Furious"],
    'runtime_movie' : [263 , 170 , 145] #in hours
}

df = pd.DataFrame(data)
sort_movies = df.sort_values("runtime_movie" , ascending=False)
print(sort_movies)
