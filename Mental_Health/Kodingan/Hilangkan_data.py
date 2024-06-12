import pandas as pd

# Membaca dataset dari file CSV
data = pd.read_csv("Mental Illness.csv")

#mendrop kolom bipolar
Drop = data.drop(columns=['bipolar'])


Drop.to_csv("Data Sementara.csv", index=False)
