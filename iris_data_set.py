# Program to download a csv file using pandas

# Import Iris Data Set csv file in pandas
# and print data  

import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/shivanand217/Iris-flower-dataset/master/iris.csv')

print(df)

