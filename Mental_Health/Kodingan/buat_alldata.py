import pandas as pd

# Membaca dataset dari file CSV
data = pd.read_csv("Data Sementara.csv")


subset_data = data[data['Entity'].isin(['China', 'Indonesia', 'India', 'Pakistan'])]

subset_data = subset_data[(subset_data['Year'] >= 2015) & (subset_data['Year'] <= 2019)]


# Menyimpan subset data ke file baru
subset_data.to_csv("all data.csv", index=False)