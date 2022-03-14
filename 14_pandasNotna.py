# Filter specific rows based on certain condition from a DataFrame
# using notna() method

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")

# Here dataset is converted to dataframe called movies

# The notna() conditional function returns a True for each row the values are 
# not an Null value. As such, this can be combined with the selection 
# brackets [] to filter the data table.

# Let get row without NA under length column in the dataframe

movie_length_notna = movies[movies["Length"].notna()]

print(movie_length_notna)


"""
Concepts learned
 - notna()
"""