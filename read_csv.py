# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:53:49 2023

@author: gabomg24
"""

import pandas 

import matplotlib.pyplot as plt

df=pandas.read_csv('happyscore_income.csv')

print(df.head())
print(len(df))
print('--------------\n')

for col in df.columns:
    print(col)
    
print('--------------\n')
print(df["avg_income"].mean())

df.hist(column='avg_income')

df[['country','avg_income']].plot.bar()
print(df['avg_income'].sort_values(ascending=True))






