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

# Bar plot untuk melihat rata-rata kejadian gangguan mental di setiap negara
average_depression = all_data.groupby('Entity')['depression'].mean()
plt.bar(average_depression.index, average_depression)
plt.title('Average Depression by Entity')
plt.ylabel('Average Depression')
plt.xlabel('Entity')
plt.show()

# Line plot untuk melihat tren kejadian gangguan mental dari waktu ke waktu di setiap negara
plt.figure(figsize=(12, 8))
for entity, data in all_data.groupby('Entity'):
    plt.plot(data['Year'], data['Anxiety'], label=entity)
plt.title('Trend of Anxiety Over Time by Entity')
plt.ylabel('Anxiety')
plt.xlabel('Year')
plt.legend(title='Entity')
plt.show()

# Scatter plot untuk melihat hubungan antara dua jenis gangguan mental
plt.figure(figsize=(12, 8))
for entity, data in all_data.groupby('Entity'):
    plt.scatter(data['bipolar'], data['depression'], label=entity)
plt.title('Relationship Between Bipolar and Depression')
plt.xlabel('Bipolar')
plt.ylabel('Depression')
plt.legend(title='Entity')
plt.show()
