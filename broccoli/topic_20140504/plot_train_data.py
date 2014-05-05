# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

def x_y_species(df, species_name):
    x_array = df[df['class'] == species_name]['x'].values
    y_array = df[df['class'] == species_name]['y'].values
    return x_array, y_array

df = pd.read_csv('xor_simple.csv')
x_array, y_array = x_y_species(df, 0)
plt.plot(x_array, y_array, 'bo')

x_array, y_array = x_y_species(df, 1)
plt.plot(x_array, y_array, 'ro')
plt.xlabel('x', fontsize=20)
plt.ylabel('y', fontsize=20)
plt.axis("tight", fontsize=20)
x_min, x_max = x_array.min() - 1, x_array.max() + 1
y_min, y_max = y_array.min() - 1, y_array.max() + 1
plt.xlim((x_min, x_max))
plt.ylim((y_min, y_max))
plt.show()
