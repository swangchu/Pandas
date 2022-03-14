# Read data from the external csv file
# Display data using tail() method

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")
# Here dataset is converted to dataframe called movies

# For each of the columns, the used data type is enlisted. The data types in this 
# DataFrame are integers (int64), floats (float64) and strings (object).
# dtypes is an attribute of a dataframe

dataTypes = movies.dtypes
print(dataTypes)
# This will display all the columns with their corresponding data types

# Shape attribute of dataframe give number of rows and columns
# (numberOfrows, numberOfcols)
row_col = movies.shape
print("Shape of the dataframe is ",row_col)

"""
Concepts learned
 - dtypes attributes
 - shape attribute

"""