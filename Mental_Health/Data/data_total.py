import pandas as pd

# Membaca dataset dari file CSV
data = pd.read_csv("all data.csv")

# Menambahkan kolom total
data['Total'] = data[['Depression', 'Schizophrenia', 'eating disorders', 'Anxiety']].sum(axis=1)

# Menyimpan data yang telah dimodifikasi ke dalam file CSV baru
data.to_csv("dataset_with_total.csv", index=False)
