# Program to import Iris_Data_SET CSV file into Python using Pandas.

import pandas as pd

page = pd.read_csv(
'https://raw.githubusercontent.com/shivanand217/Iris-flower-dataset/master/iris.csv',
# Update dataset to include header with column ID.
names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]) 

# Write dataset to text file (complete non-truncated text file).
with open ("iris_data_set.txt", "w") as f:
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', -1)
    page.head()
    f.writelines(str(page))

# Convert updated text file back to pandas dataframe 
# and print to the interpreter (non-truncated file).
page = pd.read_fwf('iris_data_set.txt')

print(page)

