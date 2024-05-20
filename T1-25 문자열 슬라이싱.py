# basic1 데이터에서 f4가 E로 시작하면서 부산에 살고 20대인 사람은 몇 명일까요?
import pandas as pd
df = pd.read_csv("data/basic1.csv")
# print(df)

# 조건
cond1 = df['f4'].str[0] == 'E'
cond2 = df['city'] == '부산'
cond3 = (df['age'] >= 20) & (df['age'] < 30)

# 결과
result = len(df[cond1 & cond2 & cond3])
print(result)
