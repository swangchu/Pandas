# Read data from the external csv file
# Display selected data using head() method

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")
# Here dataset is converted to dataframe called movies

# If we want to read first five records of the dataset
# head() method is used.
# By default head will display first five records in the dataset

defaultRows = movies.head()
print(defaultRows)

# To see the first N rows of a DataFrame, use the head() method 
# with the required number of rows (in this case 10) as argument.

tenRows = movies.head(10)
print(tenRows)

"""
Concepts learned
 - head()
 - head(N)
"""