import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari setiap negara
data_india = pd.read_csv('Data-India.csv')
data_china = pd.read_csv('Data-China.csv')
data_indonesia = pd.read_csv('Data-Indonesia.csv')
data_pakistan = pd.read_csv('Data-Pakistan.csv')

# Menambahkan kolom untuk mengidentifikasi negara
data_india['Entity'] = 'India'
data_china['Entity'] = 'China'
data_indonesia['Entity'] = 'Indonesia'
data_pakistan['Entity'] = 'Pakistan'

# Menggabungkan semua data menjadi satu DataFrame
all_data = pd.concat([data_india, data_china, data_indonesia, data_pakistan])

# Plotting
plt.figure(figsize=(12, 8))

# Bar plot untuk melihat rata-rata kejadian setiap jenis gangguan mental di setiap negara
plt.subplot(2, 3, 1)
rata_depresi = all_data.groupby('Entity')['Depression'].mean()
plt.bar(rata_depresi.index, rata_depresi)
plt.title('Rata-rata Depresi ')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Negara')
plt.grid(True)

plt.subplot(2, 3, 2)
rata_skizofrenia = all_data.groupby('Entity')['Schizophrenia'].mean()
plt.bar(rata_skizofrenia.index, rata_skizofrenia)
plt.title('Rata-rata Skizofrenia ')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Negara')
plt.grid(True)


plt.subplot(2, 3, 4)
rata_gangguan_makan = all_data.groupby('Entity')['eating disorders'].mean()
plt.bar(rata_gangguan_makan.index, rata_gangguan_makan)
plt.title('Rata-rata eating disorders ')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Negara')
plt.grid(True)

plt.subplot(2, 3, 5)
rata_kecemasan = all_data.groupby('Entity')['Anxiety'].mean()
plt.bar(rata_kecemasan.index, rata_kecemasan)
plt.title('Rata-rata anxiety')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Negara')
plt.grid(True)

plt.tight_layout()
plt.show()
