# 'f4'컬럼의 값이 'ESFJ'인 데이터를 'ISFJ'로 대체하고, 'city'가 '경기'이면서 'f4'가 'ISFJ'인 데이터 중 'age'컬럼의 최대값을 출력하시오!¶
import pandas as pd

df = pd.read_csv('data/basic1.csv')
# print(df)

# 값 변경하기
# replace('a', 'b'):'a'가 'b'로 대체
df['f4'] = df['f4'].replace('ESFJ', 'ISFJ')

# 변경 값 확인
# print(df['f4'].value_counts())

# 2개의 조건에 맞는 값중 age컬럼의 최대값
result = df.loc[(df['city']=='경기') & (df['f4'] == 'ISFJ'), 'age'].max()
print(result)