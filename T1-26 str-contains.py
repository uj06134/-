# T1-26. menu컬럼에 "라떼" 키워드가 있는 데이터의 수는?
import pandas as pd
df = pd.read_csv("data/payment.csv")
# print(df)

result = len(df[df['menu'].str.contains('라떼')])
print(result)

