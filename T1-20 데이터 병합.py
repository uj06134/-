# basic1 데이터와 basic3 데이터를 'f4'값을 기준으로 병합하고,
# 병합한 데이터에서 r2결측치를 제거한다음, 앞에서 부터 20개 데이터를 선택하고 'f2'컬럼 합을 구하시오
import pandas as pd
b1 = pd.read_csv("data/basic1.csv")
b3 = pd.read_csv("data/basic3.csv")
# print(b1, b3)

# 데이터 결합(f4를 기준으로 결합)
# pd.merge(): 두 데이터프레임을 각 데이터에 존재하는 고유값(key)을 기준으로 병합할때 사용
df = pd.merge(left = b1 , right = b3, how = "left", on = "f4")
# print(df)

# 결측치 확인
# print(df.isnull().sum())

# r2 결측치 제거
df = df.dropna(subset=['r2'])
# print(df.isnull().sum())

# 앞에서 부터 20개 데이터를 선택하고 'f2'컬럼 합
df = df.head(20)
result = df['f2'].sum()
print(result)


