# Import Python Libraries to be used in the project.
import pandas as pd
import numpy as np

# Download data set using Python Pandas.
page = pd.read_csv(
'https://raw.githubusercontent.com/shivanand217/Iris-flower-dataset/master/iris.csv',
names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]) # Update 
# dataset to include header with column ID.

# Set_option is to stop python truncating the data.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)

# Write complete non-truncated dataset to text file 
with open ("iris_data_set.txt", "w") as f:
    f.writelines(str(page))

# Output a summary of each variable to a single text file:
with open ("iris_variable_summary.txt", "w") as f:
    f.write("Descriptive statistics: using the describe method to return:\ncount; mean; std; min and max; 25%, 50%, 75% quartiles of the dataset.\n\n")
    f.write(str(page.describe()))
    
# Print modified text file including variable summary to the interpreter.
print(page)
print(page.describe())
