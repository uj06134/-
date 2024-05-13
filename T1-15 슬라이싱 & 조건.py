# 주어진 데이터 셋에서 age컬럼 상위 20개의 데이터를 구한 다음 f1의 결측치를 중앙값으로 채운다.
# 그리고 f4가 ISFJ와 f5가 20 이상인 f1의 평균값을 출력하시오.
import pandas as pd
df = pd.read_csv("data/basic1.csv")
# print(df)

# 방법 1
# age컬럼 상위 20개의 데이터
df = df.sort_values('age', ascending=False).head(20)
# print(df)

# 결측치 확인
# print(df.isnull().sum())

# # 방법 2
# # 슬라이싱
# df = df.sort_values('age', ascending=False).reset_index()
# df = df[:20]

# f1의 중앙값 구하기
med = df['f1'].median()

# 중앙값으로 결측치 채우기
df['f1'].fillna(med, inplace=True)
# print(df.isnull().sum())

# 결과
result = df.loc[(df['f4'] == 'ISFJ') & (df['f5'] >= 20), 'f1'].mean()
print(result)