import pandas as pd

data = pd.read_csv('all data.csv')

print(data.duplicated())