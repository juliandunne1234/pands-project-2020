# Import Python Libraries to be used in the project.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Download data set using Python Pandas.
df = pd.read_csv(
'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/639388c2cbc2120a14dcf466e85730eb8be498bb/iris.csv')

# Set_option is to stop python truncating the data.
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', -1)

# Write complete non-truncated dataset to text file 
with open ("iris_data_set.txt", "w") as f:
    f.writelines(str(df))

# Output a summary of each variable to a single text file:
with open ("iris_variable_analysis.txt", "w") as f:
    f.write("Descriptive statistics: using the describe method to return:\ncount; mean; std; min and max; 25%, 50%, 75% quartiles of the dataset.\n\n")
    f.write(str(df.describe()))

# Creat and save a Histogram of each variable to png files:
# Using Pythons Matplotlib Library:
plt.hist(df['sepal_length'], label='Sepal Length')
plt.legend()
plt.title('Sepal Length')
plt.xlabel('Sepal Length in cm')
plt.ylabel('Frequency')
plt.savefig('sepal_length.png')
plt.clf()

plt.hist(df['sepal_width'], label='Sepal Width')
plt.legend()
plt.title('Sepal Width')
plt.xlabel('Sepal Width in cm')
plt.ylabel('Frequency')
plt.savefig('sepal_width.png')
plt.clf()

plt.hist(df['petal_length'], label='Petal Length')
plt.legend()
plt.title('Petal Length')
plt.xlabel('Petal Length in cm')
plt.ylabel('Frequency')
plt.savefig('petal_length.png')
plt.clf()

plt.hist(df['petal_width'], label='Petal Width')
plt.legend()
plt.title('Petal Width')
plt.xlabel('Petal Width in cm')
plt.ylabel('Frequency')
plt.savefig('petal_width.png')
plt.clf()

# Create and save a Pair-Plot between each of the variables
# Using the Python Seaborn Library:
sns_plot = sns.pairplot(df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
sns_plot.savefig("iris_data_set_pairplot.png")