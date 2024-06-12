import pandas as pd

# Membaca dataset dari file CSV
data = pd.read_csv("all data.csv")


subset_data = data[data['Entity'].isin(['China'])]
subset_data = subset_data[(subset_data['Year'] >= 2015) & (subset_data['Year'] <= 2019)]

subset_data.to_csv("Data-China.csv", index=False)
