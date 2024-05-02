# 데이터에서 IQR을 활용해 Fare컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오
import pandas as pd

df = pd.read_csv('data/titanic.csv')
# print(df)

# IQR 구하기
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

# 이상치 데이터 구하기
max_out = Q3 + IQR * 1.5
min_out = Q1 - IQR * 1.5
# print(max_out, min_out)

# 이상치 데이터의 여성 수 구하기
out_df = df.loc[(df['Fare'] > max_out) | (df['Fare'] < min_out), :]
result = sum(out_df['Gender'] == 'female')
print(result)


