# Create a data frame in pandas
# Display the data frame

import pandas as pd

"""
A DataFrame is a 2-dimensional data structure that can store data of 
different types (including characters, integers, floating point values, 
categorical data and more) in columns. It is similar to a spreadsheet.

"""

# I am going to create dataframe for movie title, year of release and length of the movie in minutes.
# We will covert the table below to a dataframe in Padas
"""
   Movie                        | Year  | length in minutes
   --------------------------------------------------------
   Lunana: A Yak in Classroom   | 2019  | 110 min
   The Cup                      | 1999  | 93 min
   Milarepa                     | 2006  | 90 min
   -----------------------------------------------------------
"""
# We are creeating a dataframe and assigning to df variable
df = pd.DataFrame(
    {
        "Movie": [
            "Lunana: A Yak in Classroom",
            "The Cup",
            "Milarepa"
        ],
        "year": [2019, 1999, 2006],
        "length":[ 110, 93, 90]
    }
)

# As always to display the dataframe(df) that we have created
# we use print function

print(df)

# You will see output in the form of a table with column name 
# and rows with numbers

"""
concepts learned
 - pd.DataFrame()
 - Displaying the DataFrame
"""