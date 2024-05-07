# 주어진 데이터 셋에서 'f2' 컬럼이 1인 조건에 해당하는 데이터의 'f1'컬럼 누적합을 계산한다.
# 이때 발생하는 누적합 결측치는 바로 뒤의 값을 채우고, 누적합의 평균값을 출력한다. (단, 결측치 바로 뒤의 값이 없으면 다음에 나오는 값을 채워넣는다)
import pandas as pd
import numpy as np
df = pd.read_csv('data/basic1.csv')

# cumsum(): 누적합을 계산하는 함수
df2 = df.loc[df['f2']==1,'f1'].cumsum()
# print(df2)


# 결측치 처리 (뒤에 나오는 값으로 채움)
df2 = df2.fillna(method = 'bfill')
# df2.fillna(method='pad') # 이전값으로 채워넣는 방법
result = df2.mean()
print(result)
