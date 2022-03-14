# Filter specific rows from a DataFrame


import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")

# Here dataset is converted to dataframe called movies

# Let us get Movie and the Director from the movies dataframe
# To select multiple columns, use a list of column names within the selection brackets [].

# To select rows based on a conditional expression, 
# use a condition inside the selection brackets [].

# Let's get the movies released after the year 2000
# The condition inside the selection brackets movies["year"] > 2000 
# checks for which rows the year column has a value larger than 200:

movie_release_after_2000 = movies[movies["Year"] > 2000]

print(movie_release_after_2000)

# conditional expression (>, but also ==, !=, <, <=,… )

"""
Concepts learned
 - info() method
 - filter data from a dataframe
 
"""