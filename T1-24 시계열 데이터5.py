# 주어진 데이터(basic2.csv)에서 "pv"컬럼으로 1일 시차(lag)가 있는 새로운 컬럼을 만들고
# (예: 1월 2일에는 1월 1일 pv데이터를 넣고, 1월 3일에는 1월 2일 pv데이터를 넣음),
# 새로운 컬럼의 1월 1일은 다음날(1월 2일)데이터로 결측치를 채운 다음,
# Events가 1이면서 Sales가 1000000이하인 조건에 맞는 새로운 컬럼 합을 구하시오.
import pandas as pd
df = pd.read_csv('data/basic2.csv')
# print(df)

# 1일 차이가 나는 시차 특성 만들기
# shift(1): 'PV' 컬럼의 값을 한 행씩 아래로 이동시켜 새로운 컬럼 'previous_PV'를 만듬
df['previous_PV'] = df['PV'].shift(1)

# 1일 씩 미뤘음으로 가장 앞이 결측값이 됨 (바로 뒤의 값으로 채움)
# fillna(method='bfill'): 바로 다음 행의 값을 사용하여 NaN을 채우는 방법
df['previous_PV'] = df['previous_PV'].fillna(method = 'bfill')

# 조건에 맞는 1일 이전 PV의 합
cond = (df['Events'] == 1) & (df['Sales'] <= 1000000)
result = df.loc[cond, 'previous_PV'].sum()
print(result)