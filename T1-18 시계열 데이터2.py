# 주어진 데이터에서 2022년 5월 주말과 평일의 sales컬럼 평균값 차이를 구하시오 (소수점 둘째자리까지 출력, 반올림)
import pandas as pd
df = pd.read_csv('data/basic2.csv')
# print(df)

# 데이터 정보 확인
# print(df.info())

# datetime으로 type변경
df['Date'] = pd.to_datetime(df['Date'])

# 새로운 컬럼 추가 (년, 월, 일, 요일)
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
# 0:월, 1:화, 2:수, 3:목, 4:금, 5:토, 6:일
df['dayofweek'] = df['Date'].dt.dayofweek

# 2022년 5월 평일
m1 = df.loc[(df['month'] == 5) & (df['year'] == 2022) & (df['dayofweek'] <= 4), 'Sales'].mean()
# 2022년 5월 주말
m2 = df.loc[(df['month'] == 5) & (df['year'] == 2022) & (df['dayofweek'] >= 5), 'Sales'].mean()

# 주말과 평일의 Sales컬럼 평균값 차이 (소수점 둘째자리까지 출력, 반올림)
result = round(m2 - m1, 2)
print(result)

