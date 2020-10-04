import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('source/part3/auto-mpg.csv', header=None)

df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

df.plot(x='weight', y='mpg', kind='scatter')
plt.show()