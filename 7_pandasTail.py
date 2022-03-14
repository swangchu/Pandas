# Read data from the external csv file
# Display data using tail() method

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")
# Here dataset is converted to dataframe called movies

# pandas also provides a tail() method. 
# By default it will display last five records in the dataframe.

defaultRows = movies.tail()
print(defaultRows)

# To see the last N rows of a DataFrame, use the tail() method 
# with the required number of rows (in this case 10) as argument.

tenRows = movies.tail(10)
print(tenRows)

"""
Concepts learned
 - tail()
 - tail(N)
"""