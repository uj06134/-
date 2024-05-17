# 주어진 데이터(basic2.csv)에서 주 단위 Sales의 합계를 구하고, 가장 큰 값을 가진 주와 작은 값을 가진 주의 차이를 구하시오(절대값)
import pandas as pd
df = pd.read_csv('data/basic2.csv')

# Date 컬럼을 datetime 형식으로 변환
df['Date'] = pd.to_datetime(df['Date'])

# Date 컬럼을 인덱스로 설정
df = df.set_index('Date')

# 주 단위로 resample하여 합계를 계산
# resample(): Datetime Index를 원하는 주기로 나누어주는 메서드
df_w = df.resample('W').sum()
# print(df_w)

# 주 단위 합계에서 가장 큰 값과 가장 작은 값의 차이(절대값) 계산
max_value = df_w['Sales'].max()
min_value = df_w['Sales'].min()
result = abs(max_value - min_value)
print(result)