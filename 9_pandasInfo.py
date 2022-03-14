# Read data from the external csv file
# Display data using tail() method

import pandas as pd

# pandas provides the read_csv() function to read data stored as a csv file into a pandas DataFrame. 
# pandas supports many different file formats or data sources out of the box (csv, excel, sql, json, parquet, …), 
# each of them with the prefix read_*.

# Here we will read a csv file of Bhutanese movies

movies = pd.read_csv("Bhutanese.movies.csv")
# Here dataset is converted to dataframe called movies

# The method info() provides technical information about a DataFrame
# It gives the summary of the dataframe

summary = movies.info()
print(summary)

# OUTPUT
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50 entries, 0 to 49
Data columns (total 6 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   Movie     50 non-null     object 
 1   Length    37 non-null     float64
 2   Year      49 non-null     float64
 3   Rating    15 non-null     float64
 4   Genre     50 non-null     object 
 5   Director  47 non-null     object 
dtypes: float64(3), object(3)
memory usage: 2.5+ KB
None
"""

"""
Concepts learned
 - info() method
 
"""