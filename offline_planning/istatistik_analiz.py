import pandas as pd
from scipy import stats
import numpy as np

# Deney sonuçlarını içeren csv dosyası yükeleme
df = pd.read_csv('deney_sonuclari.csv')

# A* ve RRT verilerini ayırma
astar_sure = df[df['Algoritma'] == 'A*']['Sure_Saniye']
rrt_sure = df[df['Algoritma'] == 'RRT']['Sure_Saniye']

astar_uzunluk = df[df['Algoritma'] == 'A*']['Yol_Uzunlugu_Piksel']
rrt_uzunluk = df[df['Algoritma'] == 'RRT']['Yol_Uzunlugu_Piksel']

print("=== İSTATİSTİKSEL BULGULAR ===")

# 1. Süre Analizi
t_stat_sure, p_val_sure = stats.ttest_ind(astar_sure, rrt_sure)
print(f"\n--- Planlama Süresi ---")
print(f"A* Ortalama: {astar_sure.mean():.4f} sn (SS: {astar_sure.std():.4f})")
print(f"RRT Ortalama: {rrt_sure.mean():.4f} sn (SS: {rrt_sure.std():.4f})")
print(f"T-Testi: t = {t_stat_sure:.4f}, p = {p_val_sure:.4e}")
if p_val_sure < 0.05:
    print("Sonuç: İki algoritmanın çalışma süreleri arasında istatistiksel olarak ANLAMLI bir fark vardır (H0 Reddedildi).")
else:
    print("Sonuç: İki algoritmanın çalışma süreleri arasında anlamlı bir fark YOKTUR.")

# 2. Yol Uzunluğu Analizi
t_stat_uzunluk, p_val_uzunluk = stats.ttest_ind(astar_uzunluk, rrt_uzunluk)
print(f"\n--- Yol Uzunluğu ---")
print(f"A* Ortalama: {astar_uzunluk.mean():.2f} px (SS: {astar_uzunluk.std():.2f})")
print(f"RRT Ortalama: {rrt_uzunluk.mean():.2f} px (SS: {rrt_uzunluk.std():.2f})")
print(f"T-Testi: t = {t_stat_uzunluk:.4f}, p = {p_val_uzunluk:.4e}")
if p_val_uzunluk < 0.05:
    print("Sonuç: İki algoritmanın bulduğu yol uzunlukları arasında istatistiksel olarak ANLAMLI bir fark vardır (H0 Reddedildi).")
else:
    print("Sonuç: Yol uzunlukları arasında anlamlı bir fark YOKTUR.")