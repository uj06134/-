# min-max스케일링 기준 상하위 5% 구하기
# 주어진 데이터에서 'f5'컬럼을 min-max 스케일 변환한 후, 상위 5%와 하위 5% 값의 합을 구하시오.
# min-max스케일링: x-Min(x)/Max(x)-Min(x)

import pandas as pd
import numpy as np
from sklearn.preprocessing import power_transform
df = pd.read_csv('data/basic1.csv')
# print(df)

# min-max scale 방법1
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['f5_1'] = scaler.fit_transform(df[['f5']])

# min-max scale 방법2
df['f5_2'] = df['f5'].transform(lambda x: ((x - x.min()) / (x.max() - x.min())))

# 하위 5%, 상위 5% 값 구하기
lower = df['f5_1'].quantile(0.05)
# print(lower)

upper = df['f5_1'].quantile(0.95)
# print(upper)

result = lower + upper
print(result)