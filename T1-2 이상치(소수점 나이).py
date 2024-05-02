# 주어진 데이터에서 이상치(소수점 나이)를 찾고 올림, 내림, 버림(절사)했을때 3가지 모두 이상치 'age' 평균을 구한 다음 모두 더하여 출력하시오
import pandas as pd
import numpy as np
df = pd.read_csv('data/basic1.csv')
# print(df)

# 소수점 데이터 찾기
decimal_df = df[df['age'] % 1 != 0]
# print(decimal_df)

# 올림
# np.ceil()
m_ceil = np.ceil(decimal_df['age']).mean()
# print(m_ceil)

# 내림
# np.floor()
m_floor = np.floor(decimal_df['age']).mean()
# print(m_floor)

# 버림
# np.trunc()
m_trunc = np.trunc(decimal_df['age']).mean()
# print(m_trunc)

# 반올림
# np.round()
m_round = np.round(decimal_df['age']).mean()
# print(m_round)

# 평균값 더한 다음 출력
result = m_ceil + m_floor + m_trunc
print(result)