# 주어진 데이터에서 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균을 구하고, 그 차이를 구해보세요
# (단, 100%가 넘는 접종률 제거, 소수 첫째자리까지 출력)
import pandas as pd
df = pd.read_csv("data/covid-vaccination-vs-death_ratio.csv")
# print(df)

# 같은 국가끼리 하나의 그룹으로 묶는다.
df2 = df.groupby('country').max()
print(df2)
df2 = df2.sort_values(by='ratio', ascending = False)

# 100%가 넘는 접종률 제거
cond = df2['ratio'] <= 100
df2 = df2[cond]

# 상위 10개 국가의 접종률 평균과 하위 10개 국가의 접종률 평균
top = df2['ratio'].head(10).mean()
bottom = df2['ratio'].tail(10).mean()

# 결과
result = round(top - bottom, 1)
print(result)