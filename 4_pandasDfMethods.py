# We will look at some methods of the dataframe
# max(). min() and describe

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
print("-----------------------------------------")

# max() method gives the maximum in a given column

max_length = df["length"].max()
print("The longest duration of the movie is ", max_length,"minutes")

#min() method for finding minimum duration of a movie
min_length = df["length"].min()
print("The longest duration of the movie is ", min_length,"minutes")

#The describe() method provides a quick overview of the numerical data in a DataFrame. As the 
# Movie columns is textual data, by default not taken into account by the describe() method.

desp = df.describe()
print(round(desp,2))

"""
concepts learned
 - max()
 - min()
 - describe()
"""