# Select a subset of a DataFram
# In program 1_pandasSeries.py we have seen how to get series
# Here we are going to get more than one series


import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")

# Here dataset is converted to dataframe called movies

# Let us get Movie and the Director from the movies dataframe
# To select multiple columns, use a list of column names within the selection brackets [].

# The inner square brackets define a Python list with column names,
# whereas the outer brackets are used to select the data from a pandas 
# DataFrame as shown below.

movie_director = movies[["Movie","Director"]]

print(movie_director.head())

"""
Concepts learned
 - info() method
 
"""