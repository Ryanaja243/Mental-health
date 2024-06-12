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

# Plotting
plt.figure(figsize=(12, 8))

# Grafik untuk schizophrenia
plt.subplot(2, 2, 1)
for entity, data in data_india.groupby('Entity'):
    plt.plot(data['Year'], data['Schizophrenia'], label=entity)
plt.title('Skizofrenia ')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)

plt.subplot(2, 2, 2)
for entity, data in data_china.groupby('Entity'):
    plt.plot(data['Year'], data['Schizophrenia'], label=entity)
plt.title('Skizofrenia ')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)

plt.subplot(2, 2, 3)
for entity, data in data_indonesia.groupby('Entity'):
    plt.plot(data['Year'], data['Schizophrenia'], label=entity)
plt.title('Skizofrenia ')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)

plt.subplot(2, 2, 4)
for entity, data in data_pakistan.groupby('Entity'):
    plt.plot(data['Year'], data['Schizophrenia'], label=entity)
plt.title('Skizofrenia ')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)

plt.tight_layout()
plt.show()
