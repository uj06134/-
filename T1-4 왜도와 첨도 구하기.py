# 주어진 데이터 중 train.csv에서 'SalePrice'컬럼의 왜도와 첨도를 구한 값과,
# 'SalePrice'컬럼을 스케일링(log1p)로 변환한 이후 왜도와 첨도를 구해 모두 더한 다음 소수점 2째자리까지 출력하시오.

import pandas as pd
import numpy as np
df = pd.read_csv('data/train.csv')
# print(df)

# 'SalePrice'컬럼 왜도와 첨도계산
# skew(): 왜도
s1 = df['SalePrice'].skew()
# kurt(): 첨도
k1 = df['SalePrice'].kurt()
# print("왜도:" ,s1)
# print("첨도:" ,k1)

# 'SalePrice'컬럼 로그변환
# np.log1p(): 로그 변환
df['SalePrice'] = np.log1p(df['SalePrice'])
s2 = df['SalePrice'].skew()
k2 = df['SalePrice'].kurt()

# 소수점 2째자리까지 출력
result = round(s2 + k2, 2)
print(result)