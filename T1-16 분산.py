# 주어진 데이터 셋에서 f2가 0값인 데이터를 age를 기준으로 오름차순 정렬하고
# 앞에서 부터 20개의 데이터를 추출한 후
# f1 결측치(최소값)를 채우기 전과 후의 분산 차이를 계산하시오 (소수점 둘째 자리까지)
import pandas as pd
df = pd.read_csv('data/basic1.csv')
# print(df)

# f2가 0값인 데이터를 age를 기준으로 오름차순 정렬
df = df[df['f2']==0]
df = df.sort_values(by='age', ascending=True)

# 앞에서 부터 20개의 데이터를 추출
df = df.head(20)

# 분산 구하기
# var(): 분산 계산
df_var1 = df['f1'].var()

# 결측치 채우기(최소값)
df['f1'] = df['f1'].fillna(df['f1'].min())

# 결측치 채운 후 분산 구하기
df_var2 = df['f1'].var()

# 전과 후의 분산 차이
result = round(df_var1 - df_var2, 2)
print(result)