import pandas as pd

url = 'source/part2/sample.html'

tables = pd.read_html(url)

print(len(tables))
print('\n')

for i in range(len(tables)):
    print("tables[%s]" %i)
    print(tables[i])
    print('\n')

df = tables[1]

df.set_index(['name'], inplace=True)
print(df)
