# 2022년 5월 Sales의 중앙값을 구하시오
import pandas as pd
df = pd.read_csv('data/basic2.csv')
# print(df)

# 데이터 정보 확인
# print(df.info())

# datetime으로 type변경
df['Date'] = pd.to_datetime(df['Date'])
# print(df.info())

# 새로운 컬럼 추가 (년, 월, 일)
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
# print(df)

result = df.loc[(df['month'] == 5) & (df['year'] == 2022), 'Sales'].median()
print(result)