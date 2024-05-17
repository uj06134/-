# basic1 데이터 중 'age'컬럼 이상치를 제거하고, 동일한 개수로 나이 순으로 3그룹으로 나눈 뒤 각 그룹의 중앙값을 더하시오
# 이상치는 음수(0포함), 소수점 값

import pandas as pd
df = pd.read_csv('data/basic1.csv')
# print(df)

# 이상치 제거
# 0 이하인 행을 제외하고 나머지 행을 선택
df = df[~(df['age'] <= 0)]
# 소수점 값 제거
df = df[(df['age'] == round(df['age'], 0))]

# pd.qcut(df[col], n, labels['group-1, ... group-n']): n 개의 동일한 개수의 그룹으로 나누기
df['range'] = pd.qcut(df['age'], q=3, labels=['group1', 'group2', 'group3'])

# 수량 비교
# print(df['range'].value_counts())

# 각 그룹의 중앙값 구하기
g1_med = df[df['range'] == 'group1']['age'].median()
g2_med = df[df['range'] == 'group2']['age'].median()
g3_med = df[df['range'] == 'group3']['age'].median()

# 각 그룹의 중앙값의 합계
result = g1_med + g2_med + g3_med
print(result)

