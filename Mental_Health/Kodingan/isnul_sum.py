import pandas as pd

daata = pd.read_csv('all data.csv')
print( daata.isnull().sum())

