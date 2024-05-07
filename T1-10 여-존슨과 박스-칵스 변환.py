# 주어진 데이터에서 20세 이상인 데이터를 추출하고 'f1'컬럼을 결측치를 최빈값으로 채운 후, f1 컬럼의 여-존슨과 박스콕스 변환 값을 구하고,
# 두 값의 차이를 절대값으로 구한다음 모두 더해 소수점 둘째 자리까지 출력(반올림)하시오.

# power_transform 함수는 scikit-learn의 preprocessing 모듈에 있는 함수입니다.
# 이 함수는 데이터를 변환하기 위해 여러 변환 방법 중 'Yeo-Johnson' 또는 'Box-Cox' 변환을 선택할 수 있습니다.
import pandas as pd
import numpy as np
from sklearn.preprocessing import power_transform
df = pd.read_csv('data/basic1.csv')
# print(df)

# 20세 이상인 데이터 추출
df = df.loc[df['age']>=20, :]
# print(df.isnull().sum())

# 'f1'컬럼의 최빈값 구하기
# .mode()[0]: mode() 함수는 그 결과를 여러 개의 값으로 반환할 수 있습니다. [0]을 사용하여 첫번째 값을 가져옴
mode = df['f1'].mode()[0]
# print(mode)

# 최빈값으로 'f1' 컬럼 결측치 대체
df['f1'] = df['f1'].fillna(mode)
# print(df.isnull().sum())

# 'f1'데이터 여-존슨 yeo-johnson 값 구하기
df['y'] = power_transform(df[['f1']], standardize=False) # method 디폴트 값은 여-존슨’yeo-johnson’
# print(df['y'])

# 'f1'데이터 박스-콕스 box-cox 값 구하기
df['b'] = power_transform(df[['f1']], method='box-cox', standardize=False)
# print(df['b'])

# 두 값의 차이의 절대값
# np.abs(): 절대값
yb = np.abs(df['y']-df['b'])

# 합 후 둘째자리에서 반올림
result= round(yb.sum(), 2)
print(result)