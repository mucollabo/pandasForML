import pandas as pd
import seaborn as sns

# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.head())        # 첫 5행만 표시
print('\n')
print(type(df))
print('\n')
print(df.shape)
print('\n')

# 데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.tail())      # 마지막 5행만 표시
print('\n')
print(type(addition))
print('\n')

# 데이터프레임끼리 연산하기 (addition -df)
subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))
