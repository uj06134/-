# 주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오.
import pandas as pd
import numpy as np

df = pd.read_csv('data/basic1.csv')
# print(df)

# 표준편차 구하기
s1 = df.loc[df['f4']=='ENFJ', 'f1'].std()
s2 = df.loc[df['f4']=='INFP', 'f1'].std()

# np.abs(): 절대값
result = np.abs(s1 - s2)
print(result)