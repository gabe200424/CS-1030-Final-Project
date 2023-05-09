# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:01:16 2023

@author: gabomg24
"""

import pandas as pd

import matplotlib.pyplot as plt

# Sample data
income = [580,750,850,1200,5000,10000,18000,24000]
happiness = [2.9,3.8,4.5,4.9,5.8,6.4,7.2,7.4]

data = pd.DataFrame({'Income': income, 'Happiness': happiness})

# scatter plot
data.plot(kind='scatter', x='Income', y='Happiness')
plt.xlabel('Income')
plt.ylabel('Happiness')
plt.title('correlation of "Income vs. Happiness"')

#  Pearson correlation coefficient
correlation = data['Income'].corr(data['Happiness'], method='pearson')

print('Pearson correlation coefficient:', correlation)

plt.show()