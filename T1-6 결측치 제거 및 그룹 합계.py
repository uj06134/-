# 주어진 데이터 중 basic1.csv에서 'f1'컬럼 결측 데이터를 제거하고,
# 'city'와 'f2'를 기준으로 묶어 합계를 구하고, 'city가 경기이면서 f2가 0'인 조건에 만족하는 f1 값을 구하시오.
import pandas as pd
import numpy as np

df = pd.read_csv('data/basic1.csv')
# print(df)

# 결측치 확인
# print(df.isnull().sum())


# 결측 데이터 제거
# .dropna(subset=['col']): 결측치가 있는 데이터만 제거
df = df.dropna(subset=['f1'])
# print(df.isnull().sum())


# 그룹 합계 계산
# .groupby(['col1', 'col2'])
df2 = df.groupby(['city', 'f2']).sum()
# print(df2)

# 조건에 맞는 값 출력
result = df2.loc[('경기', 0), 'f1']
print(result)
