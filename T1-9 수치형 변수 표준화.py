# 주어진 데이터에서 'f5'컬럼을 표준화(Standardization (Z-score Normalization))하고 그 중앙값을 구하시오
# 표준화 공식: z = x-μ/σ
import pandas as pd
df = pd.read_csv('data/basic1.csv')
# print(df)

# 표준편차 구하기
std = df['f5'].std()
# print(std)

# 평균 구하기
mean = df['f5'].mean()
# print(mean)

# 표준화 값 구하기
z = (df['f5'] - mean)/std
# print(z)

# 중앙값 구하기
result = z.median()
print(result)

# # sklearn 모듈 이용
# from sklearn.preprocessing import StandardScaler
#
# scaler = StandardScaler()
# df['f5'] = scaler.fit_transform(df[['f5']])
#
# # 중앙값 출력
# print(df['f5'].median())