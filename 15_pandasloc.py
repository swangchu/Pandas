# select specific rows and columns from a DataFrame
# using loc() method

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

# loc is label-based, which means that we have to specify the name of the rows and columns 
# that we need to filter out.

# Displays all records and all columns of the dataframe with movie duration 
# greater than or equal to 100 minutes
movie_all_length_100 = movies.loc[movies["Length"]>=100]
print(movie_all_length_100)

# List names of the movies with duration more than 100 minutes
movie_length_100 = movies.loc[movies["Length"]>=100, "Movie"]
print(movie_length_100)

# select with multiple conditions
# Lets select movie with 100 min or more and whose genre is drama
movie_length_drama_100 = movies.loc[(movies.Length >=100) & (movies.Genre == "Drama")]
print(movie_length_drama_100)

# select a range of rows of a dataset
# This will select row 1,2, and 3.
movie_rows_1to3 = movies.loc[1:3]
print(movie_rows_1to3)

# Select only the required columns with a condition
# Lets select movie name and director whose movie duration is less than 100 minutes
movie_movie_director_less_1000 = movies.loc[(movies.Length < 100),['Movie','Director']]
print(movie_movie_director_less_1000)

# You might have observed in the length column of the dataframe there are NaN value,
# using loc to update NaN will not work.
# we will use fillna() method to update it

movies.loc[(movies.Genre == "Documentary"),['Genre']]= "Docm"
print(movies)

# Update the values of a particular column on selected rows
# Lets update genre of movie with Documentry to Docm in the dataframe
movies['Length']= movies['Length'].fillna(0)
print(movies)


# When using the column names, row labels or a condition expression, 
# use the loc operator in front of the selection brackets []. 
# For both the part before and after the comma, you can use a single label, 
# a list of labels, a slice of labels, a conditional expression or a colon. 
# Using a colon specifies you want to select all rows or columns.

"""
Concepts learned
 - loc()
 - select row with a condition
 - slect rows with a range
 - slect the required columns with a condition
 - update the value in a column
 - fillna() method to update NaN (Not a Number) values
"""