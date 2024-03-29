# -*- coding: utf-8 -*-
"""Prodigy_DS_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BTHzK-PwGhLah9j1aSGPFX3si1fsqewm
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv(r"/content/drive/MyDrive/Colab Notebooks/Data/Internship/API_SP.POP.TOTL_DS2_en_csv_v2_6508519.csv")
df1

df1.head(10)

df1.columns

df2 = df1.drop(['Country Code', 'Indicator Name', 'Indicator Code'],axis = 1)
df2

ind = df1['Country Name'].isin(['India']).any()
ind

cont = df2[df2['Country Name'] == 'India']
cont

cont.columns

cd1 = df2[df2['Country Name'] == 'India']

years = cd1.columns[2:].astype(int)
population = cd1.iloc[0, 2:].astype(int)

plt.figure(figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Population')
plt.title(f'Population of India Over Years (1960 - 2020)')

plt.bar(years,population,color='lightgreen',edgecolor='black')
plt.show()

plt.hist(population, bins=20, color='lightgreen', edgecolor='black')
plt.show()

