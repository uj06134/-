# 문제 1
# 데이터셋(basic1.csv)의 'f5'컬럼을 기준으로 상위 10개의 데이터를 구하고,
# 'f5'컬럼 10개 중 최소값으로 데이터를 대체한 후,
# 'age'컬럼에서 80 이상인 데이터의 'f5'컬럼 평균값 구하기
import pandas as pd
df = pd.read_csv("data/basic1.csv")

# 'f5'컬럼을 기준으로 내림차순 정렬
df = df.sort_values('f5', ascending=False)
# 상위 10개의 데이터
df.head(10)
# print(df.head(10))

# 최소값
min = df['f5'][:10].min()
# print(min)

# 'f5'컬럼 10개 중 최소값으로 데이터를 대체
df.loc[10:19, 'f5'] = min
# print(df.head(10))

# 'age'컬럼에서 80 이상인 데이터의 'f5'컬럼 평균값 구하기
result1 = df.loc[df['age']>=80, 'f5'].mean()
print(result1)

# ---------------------------------------------------------------
# 문제 2
# 데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서,
# 'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고
# 두 표준편차 차이 계산하기
df = pd.read_csv("data/basic1.csv")

# 데이터 나누기
data_70 = df.iloc[:70]
# data_30 = df.iloc[70:]

# 결측치 개수 확인
# isnull().sum(): isnull과 sum 함수를 연계하면서 각 열의 결측값 개수를 간단하게 구할 수 있습니다.
data_70.isnull().sum()
# print(data_70.isnull().sum())

# 결측치 채우기 전 f1컬럼 표준편자
# std(): 표준편차
std1 = data_70['f1'].std()
# print(std1)

# 중앙값 확인
med = data_70['f1'].median()
# print(med)

# 결측히 중앙값으로 채우기
# fillna(): DataFrame에서 결측값을 원하는 값으로 변경하는 메서드
data_70['f1'] = data_70['f1'].fillna(med)

# 중앙값으로 채워졌는지 확인
data_70.isnull().sum()
# print(data_70.isnull().sum())

# 결측치 채운 후 f1컬럼 표준편자
std2 = data_70['f1'].std()
# print(std2)

# 두 표준편차 차이 계산하기
result2 = std1 - std2
print(result2)

# ---------------------------------------------------------------
# 문제3
# 데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
# 단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함
df = pd.read_csv("data/basic1.csv")

# age컬럼의 평균, 표준편차 구하기
mean = df['age'].mean()
std = df['age'].std()

# 이상치의 최대와 최소 구하기
max_out = mean + std * 1.5
min_out = mean - std * 1.5

# 'age'컬럼의 이상치 더하기
result3 = df.loc[(df['age'] > max_out) | (df['age'] < min_out), 'age'].sum()
print(result3)
