# Filter specific rows based on certain condition from a DataFrame
# using isin() methods

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")

# Here dataset is converted to dataframe called movies

# Similar to the conditional expression, the isin() conditional function 
# returns a True for each row the values are in the provided list. 
# To filter the rows based on such a function, use the conditional function 
# inside the selection brackets []

# Let get all the rows of movies which Drama or Romanace
# form the movies dataframe

movie_drama_romance = movies[movies["Genre"].isin(["Drama","Romance"])]

print(movie_drama_romance)


"""
Concepts learned
 - isin() method
"""