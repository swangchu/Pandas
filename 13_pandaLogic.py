# Filter specific rows based on certain condition from a DataFrame
# using logical operators

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")

# Here dataset is converted to dataframe called movies

# When combining multiple conditional statements, each condition must be 
# surrounded by parentheses (). Moreover, you can not use or/and but need 
# to use the or operator | and the and operator &.

# Let get all the rows of movies which is Drama and released in year 2000
# form the movies dataframe

movie_drama_2000 = movies[(movies["Genre"]=="Drama") & (movies["Year"]== 2010)]

print(movie_drama_2000)


"""
Concepts learned
 - logical operator 
"""