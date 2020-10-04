import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('source/part3/남북한발전전력량.xlsx')

df_ns = df.iloc[[0, 5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head())
print('\n')

df_ns.plot()

tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()
plt.show()