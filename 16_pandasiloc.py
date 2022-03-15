# select specific rows and columns from a DataFrame
# using iloc() method is similar to loc() 
# iloc() is indexed based while loc() is column label based

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")

# Here dataset is converted to dataframe called movies

# In this case, a subset of both rows and columns is made in one go 
# and just using selection brackets [] is not sufficient anymore. 
# The loc/iloc operators are required in front of the selection brackets [].
#  When using loc/iloc, the part before the comma is the rows you want, and 
# the part after the comma is the columns you want to select.

# List the rows and column based on their index slice

# iloc is integer index-based. So here, we have to specify rows and columns by their integer index.

movie_row9to15andCol0to2 = movies.iloc[9:15, 0:2]

# row from 9 to 14, 15th row will be excluded
# column 0 and 1, 2nd column will be excluded
# although there are column names, it is also referrenced by indexes

print(movie_row9to15andCol0to2)

# When using the column names, row labels or a condition expression, 
# use the loc operator in front of the selection brackets []. 
# For both the part before and after the comma, you can use a single label, 
# a list of labels, a slice of labels, a conditional expression or a colon. 
# Using a colon specifies you want to select all rows or columns.

"""
Concepts learned
 - iloc()
"""