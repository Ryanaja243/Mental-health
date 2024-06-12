import pandas as pd
import matplotlib.pyplot as plt

data_China = pd.read_csv('Data-China.csv')


plt.subplot(2, 2, 1)
for entity, data in data_China.groupby('Entity'):
    plt.plot(data['Year'], data['Depression'], label=entity)
plt.title('Depression dari Waktu ke Waktu')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)

plt.subplot(2, 2, 2)
for entity, data in data_China.groupby('Entity'):
    plt.plot(data['Year'], data['Schizophrenia'], label=entity)
plt.title('Schizophrenia dari Waktu ke Waktu')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)

plt.subplot(2, 2, 3)
for entity, data in data_China.groupby('Entity'):
    plt.plot(data['Year'], data['eating disorders'], label=entity)
plt.title('eating disorders dari Waktu ke Waktu')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)

plt.subplot(2, 2, 4)
for entity, data in data_China.groupby('Entity'):
    plt.plot(data['Year'], data['Anxiety'], label=entity)
plt.title('Anxiety dari Waktu ke Waktu')
plt.ylabel('Angka (per 50.000 orang)')
plt.xlabel('Tahun')
plt.legend(title='Negara')
plt.grid(True)


plt.suptitle('Grafik Data China')
plt.tight_layout()
plt.show()