import pandas as pd

Data_China = pd.read_csv('Data-China.csv')
print("Data Negara China")
print(Data_China.describe().T)


Data_India = pd.read_csv('Data-India.csv')
print("Data Negara India")
print(Data_India.describe().T)

Data_Indonesia = pd.read_csv('Data-Indonesia.csv')
print("Data Negara Indonesia")
print(Data_Indonesia.describe().T)

Data_Pakistan = pd.read_csv('Data-Pakistan.csv')
print("Data Negara Pakistan")
print(Data_Pakistan.describe().T)